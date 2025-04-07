"""These are the application schemas"""

from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    """Base User Schema"""
    username: str
    class Config:
        """Extra Configs"""
        from_attributes = True

class UserCreate(UserBase):
    """Add fields needed for creation"""
    password: str
    email: str
    phone: str
    fullname: str | None

class UserResponse(UserBase):
    """Return after login"""
    id: UUID
    created_at: datetime
    updated_at: datetime

class UserDetails(UserResponse):
    """All relevant user details"""
    phone: str
    email: str
    is_active: bool
    fullname: str | None
