"Quiz Schemas, Helps to conform to these standards in the routes"
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

class QuizSchema(BaseModel):
    """Base Quiz Model"""
    title: str
    published: bool

    class Config:
        """Used to add extra configurations that this schema must conform too"""
        str_strip_whitespace = True #remove starting and trailing spaces
        str_min_length = 1 #minimum string length is 1
        from_attributes = True

class QuizUpdate(QuizSchema):
    """Used to update a quiz"""
    id: UUID
    active: bool | None = None

class QuizCreateResponse(QuizSchema):
    """After creation, I return these details"""
    id: UUID
    created_at: datetime
    create_uid: UUID

class QuizUpdateResponse(QuizSchema):
    """After updates, I return these details"""
    id: UUID
    updated_at: datetime
    update_uid: UUID

class QuizDetails(QuizSchema):
    """This makes sure I return all information on a quiz"""
    id: UUID
    created_at: datetime
    updated_at: datetime
    create_uid: UUID
    update_uid: UUID
