"""All question related routes for execution"""
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.dependencies.auth_dependencies import get_current_user
from app.schemas.question_schemas import QuestionSchema, QuestionCreateResponse,QuestionSchemaUpdate, QuestionUpdateResponse
from app.utils.database import get_db
from app.crud import question_crud
from app.models.user_model import Users as UserModel


router = APIRouter(prefix="/question", tags=['question'])

@router.post('/', response_model=QuestionCreateResponse)
def new_question(question: QuestionSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    """Received the data for a new question"""
    return question_crud.create_question(db, question, current_user)

@router.post('/update', response_model=QuestionUpdateResponse)
def update_question(question: QuestionSchemaUpdate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    """Received the data for a new quiz"""
    return question_crud.update_question(db, question, current_user)
