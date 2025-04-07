"""This file should contain dependencies"""
from typing import Any, Dict
from datetime import datetime, timezone, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import jwt
from jose.exceptions import JWTError
from sqlmodel import Session
from app.schemas.auth_schemas import TokenData
from app.schemas.user_schemas import UserResponse
from app.crud import user_crud
from app.utils.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from app.utils.database import get_db
from app.utils.exceptions import raise_unauthorized

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Function used to verify the passwrd"""
    return pwd_context.verify(plain_password, hashed_password) #type: ignore

def get_password_hash(password: str) -> str:
    """Hashes password"""
    return pwd_context.hash(password) #type: ignore

def create_access_token(data: Dict[str, Any], expires_delta: timedelta | None = None):
    """Creates the access tokens"""
    to_encode: Dict[str, Any] = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode["exp"] = expire
    encoded_jwt: str = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def authenticate_user(db:Session, username: str, password:str):
    """Authenticate the user"""
    user = user_crud.get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> UserResponse:
    """Get current logged in user"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise raise_unauthorized("Could not validate credentials")
        token_data = TokenData(username=username)
    except JWTError as exc:
        raise raise_unauthorized("Could not validate credentials") from exc
    except jwt.exceptions.ExpiredSignatureError as exc:
        raise raise_unauthorized("Session expired") from exc
    user = user_crud.get_user_by_username(db, username = token_data.username)
    if user:
        return UserResponse.model_validate(user)
    raise raise_unauthorized("Could not validate credentials")
