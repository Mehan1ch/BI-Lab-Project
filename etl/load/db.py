import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
load_dotenv()

# Retrieve database configuration from environment variables
username = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
host = "localhost"  # Update if using a different host
port = 3306  # Default MySQL port
database = os.getenv("MYSQL_DATABASE")

# Create the connection string
connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"

# Create the SQLAlchemy engine
engine = create_engine(connection_string)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
