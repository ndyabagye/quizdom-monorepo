"""Users Router"""
from uuid import UUID
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.crud import user_crud
from app.schemas import user_schemas
from app.utils import database

from app.models.user_model import Users as UserModel
from app.dependencies.auth_dependencies import get_current_user

router = APIRouter(prefix="/user", tags=['users'])

@router.get("/me", response_model=user_schemas.UserResponse)
def read_users_me(current_user: UserModel = Depends(get_current_user)):
    "Read Users Me"
    return current_user

@router.get("/{user_id}", response_model=user_schemas.UserResponse)
def get_user(user_id: UUID, db: Session = Depends(database.get_db)):
    "Read User Route"
    return user_crud.get_user_by_id(db, user_id)
