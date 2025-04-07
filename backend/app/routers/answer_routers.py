"""All answer related routes for execution"""
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.dependencies.auth_dependencies import get_current_user
from app.schemas.answer_schemas import AnswerSchema, AnswerCreateResponse, AnswerSchemaUpdate, AnswerUpdateResponse
from app.utils.database import get_db
from app.crud import answer_crud
from app.models.user_model import Users as UserModel


router = APIRouter(prefix="/answer", tags=['answer'])

@router.post('/', response_model=AnswerCreateResponse)
def new_answer(answer: AnswerSchema, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    """Received the data for a new answer"""
    return answer_crud.create_answer(db, answer, current_user)

@router.post('/update', response_model=AnswerUpdateResponse)
def update_answer(answer: AnswerSchemaUpdate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    """Received the data for a new quiz"""
    return answer_crud.update_answer(db, answer, current_user)
