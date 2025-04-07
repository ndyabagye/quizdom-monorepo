"""All auth routes. Register and login"""

#Imports from Base Python and 3rd Party Libraries
from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

#imports from my files
from app.schemas import user_schemas, auth_schemas
from app.utils.database import get_db
from app.crud import user_crud
from app.dependencies import auth_dependencies

router = APIRouter(prefix='/auth', tags=['auth'])

@router.post("/token", response_model=auth_schemas.Token)
def login_for_success_token(form_data: OAuth2PasswordRequestForm = Depends(),
                            db: Session = Depends(get_db)):
    "Login after success"
    user = auth_dependencies.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Incorrect Username or Password",
            headers = {"WWW-Authenticate":"Bearer"},
        )
    access_token = auth_dependencies.create_access_token(data={'sub': user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post('/signup', response_model=user_schemas.UserResponse)
def signup(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    "Signup Functionality"
    db_user = user_crud.create_user(db, user)
    return db_user
