"""Answer Crud methods"""

from uuid import UUID
from fastapi import HTTPException
from sqlmodel import Session, select
from app.models.answer_model import Answer
from app.models.user_model import Users as UserModel
from app.schemas.answer_schemas import AnswerSchema, AnswerSchemaUpdate

def get_answer_by_id(db:Session, answer_id:UUID):
    """Get the answer by id"""
    return db.exec(select(Answer).where(Answer.id == answer_id)).first()

def get_answer_by_value(db: Session, value: str, question_id: UUID):
    """Get Answer by the Title"""
    return db.exec(select(Answer).where(Answer.value == value).where(Answer.question_id == question_id)).first()

def create_answer(db:Session, answer: AnswerSchema, current_user: UserModel):
    """Create Answer"""
    db_answer = get_answer_by_value(db, answer.value, answer.question_id)
    if db_answer:
        raise HTTPException(status_code=400, detail="This answer already exists")
    db_answer = Answer(
        **answer.model_dump(),
        create_uid = current_user.id,
        update_uid = current_user.id
    )
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer

def update_answer(db:Session, answer: AnswerSchemaUpdate, current_user: UserModel):
    """Used to update a quiz"""
    db_answer = get_answer_by_id(db, answer_id = answer.id)
    if not db_answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    db_answer_dict = answer.model_dump(exclude_unset=True)
    for key, value in db_answer_dict.items():
        if key == 'id':
            continue
        setattr(db_answer, key, value)
    db_answer.update_uid = current_user.id
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer
