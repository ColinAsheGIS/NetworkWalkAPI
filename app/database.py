from dotenv import load_dotenv
from sqlalchemy import create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

# Class constants
load_dotenv()
DB_USER = os.getenv('USER') #Not hardcoded
DB_PASS = os.getenv('PASSWORD')
DB_HOST = os.getenv('HOST')
DB_PORT = os.getenv('PORT')
DB_DATABASE = os.getenv('DATABASE')
DB_DIALECT = os.getenv('DB_DIALECT')

# Connect with sqlalchemy using databaseurl
engine = create_engine(f"{DB_DIALECT}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}")

# Class that can be instantiated to create a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# here base
Base = declarative_base()