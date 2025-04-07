"""Question Crud methods"""

from uuid import UUID
from fastapi import HTTPException
from sqlmodel import Session, select
from app.models.question_model import Question
from app.models.user_model import Users as UserModel
from app.schemas.question_schemas import QuestionSchema, QuestionSchemaUpdate

def get_question_by_id(db:Session, question_id:UUID):
    """Get the question by id"""
    return db.exec(select(Question).where(Question.id == question_id)).first()

def get_question_by_title(db: Session, title: str, quiz_id: UUID):
    """Get Question by the Title"""
    return db.exec(select(Question).where(Question.title == title).where(Question.quiz_id == quiz_id)).first()

def create_question(db:Session, question: QuestionSchema, current_user: UserModel):
    """Create Question"""
    db_question = get_question_by_title(db, question.title, question.quiz_id)
    if db_question:
        raise HTTPException(status_code=400, detail="This question already exists")
    db_question = Question(
        **question.model_dump(),
        create_uid = current_user.id,
        update_uid = current_user.id
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def update_question(db:Session, question: QuestionSchemaUpdate, current_user: UserModel):
    """Used to update a quiz"""
    db_question = get_question_by_id(db, question_id = question.id)
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    db_question_dict = question.model_dump(exclude_unset=True)
    for key, value in db_question_dict.items():
        if key == 'id':
            continue
        setattr(db_question, key, value)
    db_question.update_uid = current_user.id
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question
