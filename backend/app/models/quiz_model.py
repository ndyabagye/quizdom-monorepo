"""This is the base quiz model"""
from uuid import UUID, uuid4
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import text, DateTime, Column
# from app.models.question_model import Question


class Quiz(SQLModel, table=True):
    """QUiz model"""
    __table_args__ = {'extend_existing': True}

    id: UUID = Field(primary_key=True, default_factory= uuid4, nullable=False)
    title: str = Field(nullable=False, unique=True)
    published: bool = Field(default=False)
    active: bool = Field(default=True)
    questions: list["Question"] = Relationship(back_populates="quiz") # type: ignore
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
