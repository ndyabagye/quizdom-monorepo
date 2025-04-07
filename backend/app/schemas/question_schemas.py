"Question Schemas, Helps to conform to these standards in the routes"
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

class QuestionSchema(BaseModel):
    """Base Question Model"""
    title: str
    quiz_id: UUID

    class Config:
        """Used to add extra configurations that this schema must conform too"""
        str_strip_whitespace = True #remove starting and trailing spaces
        str_min_length = 1 #minimum string length is 1
        from_attributes = True

class QuestionSchemaUpdate(BaseModel):
    """Used to update a quiz"""
    id: UUID
    title: str
    active: bool | None = None

    class Config:
        """Used to add extra configurations that this schema must conform too"""
        str_strip_whitespace = True #remove starting and trailing spaces
        str_min_length = 1 #minimum string length is 1
        from_attributes = True


class QuestionCreateResponse(QuestionSchema):
    """After creation, I return these details"""
    id: UUID
    created_at: datetime
    create_uid: UUID

class QuestionUpdateResponse(QuestionSchema):
    """After updates, I return these details"""
    id: UUID
    updated_at: datetime
    update_uid: UUID

class QuestionDetails(QuestionSchema):
    """This makes sure I return all information on a Question"""
    id: UUID
    active: bool
    created_at: datetime
    updated_at: datetime
    create_uid: UUID
    update_uid: UUID
