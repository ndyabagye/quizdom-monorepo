"""All quiz related routes for execution"""
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.dependencies.auth_dependencies import get_current_user
from app.schemas.quiz_schemas import QuizSchema, QuizCreateResponse, QuizUpdate, QuizUpdateResponse
from app.utils.database import get_db
from app.crud import quiz_crud
from app.models.user_model import Users as UserModel


router = APIRouter(prefix="/quiz", tags=['quiz'])

@router.post('/', response_model=QuizCreateResponse)
def new_quiz(quiz: QuizSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    """Received the data for a new quiz"""
    return quiz_crud.create_quiz(db, quiz, current_user)

@router.post('/update', response_model=QuizUpdateResponse)
def update_quiz(quiz: QuizUpdate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    """Received the data for a new quiz"""
    return quiz_crud.update_quiz(db, quiz, current_user)
