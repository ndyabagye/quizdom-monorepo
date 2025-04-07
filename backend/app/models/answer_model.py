"""Main answer model"""
from uuid import UUID, uuid4
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import text, DateTime, Column
from app.models.question_model import Question


class Answer(SQLModel, table=True):
    """Answers Model"""
    __table_args__ = {'extend_existing': True}

    id: UUID = Field(default_factory= uuid4, unique=True, primary_key=True, nullable=False)
    value: str
    is_correct: bool = Field(default=False)
    question_id: UUID = Field(foreign_key="question.id")
    question: Question = Relationship(back_populates="answers")
    active: bool = Field(default=True)
    create_uid: UUID = Field(foreign_key="users.id")
    update_uid: UUID = Field(foreign_key="users.id")
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
