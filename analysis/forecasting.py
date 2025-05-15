# %% tags=["parameters"]
upstream = ['load_weather', 'load_diagnoses', 'load_locations']
product: list[str] | None = None

# %%

import numpy as np
import pandas as pd
from keras import Input
from keras.src.callbacks import EarlyStopping
from sklearn.preprocessing import StandardScaler
from sqlalchemy import and_, func
from sqlalchemy.exc import SQLAlchemyError
from tensorflow import keras
from tensorflow.keras import layers

from analysis.model.prediction import Prediction
from etl.load.db import SessionLocal
from etl.load.db import engine
from etl.load.models.diagnoses import Diagnosis
from etl.load.models.locations import Location
from etl.load.models.weather import Weather


def process_xy(raw_x: np.array, raw_y: np.array, look_back: int) -> np.array:
    X = np.empty(shape=(raw_x.shape[0] - look_back, look_back, raw_x.shape[1]), dtype=np.float32)
    y = np.empty(shape=(raw_y.shape[0] - look_back), dtype=np.float32)

    target_index = 0
    for i in range(look_back, raw_x.shape[0]):
        X[target_index] = raw_x[i - look_back: i]
        y[target_index] = raw_y[i]
        target_index += 1

    return X.copy(), y.copy()


session = SessionLocal()

# Diagnosis count per day around the world
query = (
    session.query(
        Weather.last_updated,
        (func.count(Diagnosis.id)).label("diagnosis_count"),
    )
    .join(
        Diagnosis,
        and_(
            Weather.temperature_category_id == Diagnosis.temperature_category_id,
        )
    )
    .join(Location,
          and_(
              Weather.location_id == Location.id,
              Location.name == "Budapest"
          )
          )
    .group_by(Weather.last_updated)
    .all()
)

# Convert the query result into a DataFrame
df = pd.DataFrame(query)

# Convert to datetime
df['last_updated'] = pd.to_datetime(df['last_updated'])

# Set index
df.set_index('last_updated', inplace=True)

# Transform dates
df["Day.Of.Year.X"], df["Day.Of.Year.Y"] = np.sin(2 * np.pi * df.index.day_of_year / 365), np.cos(
    2 * np.pi * df.index.day_of_year / 365)

# Convert the column to float
df["diagnosis_count"] = df["diagnosis_count"].astype(float)

# Compute Q1 (25th percentile) and Q3 (75th percentile)
Q1 = df["diagnosis_count"].quantile(0.25)
Q3 = df["diagnosis_count"].quantile(0.75)

# Compute IQR
IQR = Q3 - Q1

# Define lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers
df = df[(df["diagnosis_count"] >= lower_bound) & (df["diagnosis_count"] <= upper_bound)]

# Set various data starting points
train_start = pd.Timestamp("2024-05-16")
valid_start = pd.Timestamp("2025-01-01")
test_start = pd.Timestamp("2025-04-01")
train_df = df[(df.index >= train_start) & (df.index < valid_start)].copy()
valid_df = df[(df.index >= valid_start) & (df.index < test_start)].copy()
test_df = df[(df.index >= test_start)].copy()

# Scaling for target variables

scaler_input_count = StandardScaler()
scaler_output_count = StandardScaler()

scaled_train_count = scaler_input_count.fit_transform(train_df[["diagnosis_count"]])
target_train_count = scaler_output_count.fit_transform(train_df[["diagnosis_count"]])
scaled_valid_count = scaler_input_count.transform(valid_df[["diagnosis_count"]])
target_valid_count = scaler_output_count.transform(valid_df[["diagnosis_count"]])
scaled_test_count = scaler_input_count.transform(test_df[["diagnosis_count"]])
target_test_count = scaler_output_count.transform(test_df[["diagnosis_count"]])

# Set loopback for training, validation and testing

lookback = 10

train_X_count, train_y_count = process_xy(scaled_train_count, target_train_count, look_back=lookback)
valid_X_count, valid_y_count = process_xy(scaled_valid_count, target_valid_count, look_back=lookback)
test_X_count, test_y_count = process_xy(scaled_test_count, target_test_count, look_back=lookback)

# Model
model_count = keras.Sequential(
    [
        Input(shape=train_X_count.shape[1:]),
        layers.LSTM(16, activation="relu"),
        layers.Dense(1),
    ]
)
# Compile model
model_count.compile(loss='MeanSquaredError', optimizer='Adam')

# Summarize
model_count.summary()

# Callbacks
callbacks = [EarlyStopping(monitor="val_loss", patience=10)]

# Fitting the model
history_count = model_count.fit(
    train_X_count,
    train_y_count,
    validation_data=(valid_X_count, valid_y_count),
    batch_size=16,
    epochs=100,
    callbacks=callbacks,
    shuffle=True,
    verbose=False,
)

# Save results to database
pred_count = model_count.predict(test_X_count)
timestamps = test_df.index[lookback:]
real_values = test_df["diagnosis_count"].values[lookback:]
predicted_values = scaler_output_count.inverse_transform(pred_count[:len(timestamps)]).flatten()

# Create table if it doesn't exist
Prediction.__table__.create(bind=engine, checkfirst=True)

try:
    # Iterate and save predictions
    for timestamp, real, predicted in zip(timestamps, real_values, predicted_values):
        prediction = Prediction(
            timestamp=timestamp,
            real_diagnosis_count=int(real),
            predicted_diagnosis_count=int(predicted)
        )
        session.add(prediction)

    # Commit the session
    session.commit()
except SQLAlchemyError as e:
    # Rollback in case of error
    session.rollback()
    print("Error occurred while saving predictions.")
finally:
    # Close the session
    session.close()
