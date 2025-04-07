"""Database configurations"""
from fastapi import Depends
from sqlmodel import create_engine, SQLModel,Session
from app.utils.config import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

def init_db():
    """Used to initialise DB and create tables. Ideally called once for efficiency"""
    SQLModel.metadata.create_all(bind=engine)

def get_session():
    """Get session and perform functions: This is a connection to the database"""
    with Session(engine) as session:
        yield session

def get_db(session: Session = Depends(get_session)):
    """Gets the database session"""
    try:
        yield session
    finally:
        pass
