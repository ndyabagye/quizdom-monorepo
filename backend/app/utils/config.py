"""Configurations used throughout application"""

from dotenv import load_dotenv
import os

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://user:password@localhost/dbname")
SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30