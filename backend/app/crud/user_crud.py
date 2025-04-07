"""CRUD operations"""
from uuid import UUID
from fastapi import HTTPException
from sqlmodel import Session, select
from app.models.user_model import Users as UserModel
from app.schemas.user_schemas import UserCreate
from app.dependencies import auth_dependencies

def create_user(db:Session, user: UserCreate):
    """Create User"""
    db_user = get_user_by_username(db, username = user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = auth_dependencies.get_password_hash(user.password)
    # model.dump converts object to dictionary
    # items() makes it an iterable list
    # ** unpcacks the subsequent dictionary into arguments
    db_user = UserModel(
        **{k:v for k,v in user.model_dump().items() if k != 'password'},
        hashed_password = hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: UUID):
    """Read User"""
    return db.exec(select(UserModel).where(UserModel.id == user_id)).first()

def get_user_by_username(db: Session, username: str):
    """Read User"""
    return db.exec(select(UserModel).where(UserModel.username == username)).first()
