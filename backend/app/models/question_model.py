"""This is the base question model"""

from uuid import UUID, uuid4
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import text, DateTime, Column
# from app.models.answer_model import Answer
from app.models.quiz_model import Quiz

class Question(SQLModel, table=True):
    """Question Model"""
    __table_args__ = {'extend_existing': True}

    id: UUID = Field(primary_key=True, default_factory= uuid4, nullable=False)
    title: str = Field(nullable=False)
    quiz_id: UUID = Field(foreign_key="quiz.id")
    quiz: Quiz = Relationship(back_populates='questions')
    answers: list["Answer"] = Relationship(back_populates="question") # type: ignore
    active: bool = Field(default=True)
    create_uid: UUID = Field(foreign_key='users.id')
    update_uid: UUID = Field(foreign_key='users.id')
    created_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),  # Ensures TIMESTAMP WITH TIME ZONE
            server_default=text("CURRENT_TIMESTAMP")
        )
    )
    updated_at: datetime = Field(
        sa_column= Column(
            DateTime(timezone=True),
            server_default=text("CURRENT_TIMESTAMP"),
            onupdate = text('CURRENT_TIMESTAMP')
        )
    )
