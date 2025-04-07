"""Quiz CRUD methods"""

from uuid import UUID
from fastapi import HTTPException
from sqlmodel import Session, select
from app.models.quiz_model import Quiz
from app.models.user_model import Users as UserModel
from app.schemas.quiz_schemas import QuizSchema, QuizUpdate

def get_quiz_by_id(db:Session, quiz_id:UUID):
    """Get the quiz by id"""
    return db.exec(select(Quiz).where(Quiz.id == quiz_id)).first()

def get_quiz_by_title(db: Session, title: str):
    """Get Quiz by the Title"""
    return db.exec(select(Quiz).where(Quiz.title == title)).first()

def create_quiz(db:Session, quiz: QuizSchema, current_user: UserModel):
    """Create Quiz"""
    db_quiz = get_quiz_by_title(db, title = quiz.title)
    if db_quiz:
        raise HTTPException(status_code=400, detail="This quiz already exists")
    db_quiz = Quiz(
        **quiz.model_dump(),
        create_uid = current_user.id,
        update_uid = current_user.id
    )
    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz

def update_quiz(db:Session, quiz: QuizUpdate, current_user: UserModel):
    """Used to update a quiz"""
    db_quiz = get_quiz_by_id(db, quiz_id = quiz.id)
    if not db_quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    db_quiz_dict = quiz.model_dump(exclude_unset=True)
    for key, value in db_quiz_dict.items():
        if key == 'id':
            continue
        setattr(db_quiz, key, value)
    db_quiz.update_uid = current_user.id
    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz

