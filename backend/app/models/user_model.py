"""All models for the application"""
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel
from sqlalchemy import text, Column,DateTime

class Users(SQLModel, table=True):
    """Main User Model"""
    __table_args__ = {'extend_existing': True}

    id: UUID = Field(primary_key=True, default_factory= uuid4, nullable=False)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True)
    phone: str = Field(unique=True)
    fullname: Optional[str] = None
    hashed_password: str
    is_active: str = Field(default=True)

    ##----Use these if you want to delegate timestamp creation to psql, but does not
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
