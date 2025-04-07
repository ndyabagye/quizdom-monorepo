"Pydantic models"

from app.schemas.user_schemas import BaseModel

#=======TOKEN========#
class Token(BaseModel):
    """Actual Token"""
    access_token : str
    token_type: str

class TokenData(BaseModel):
    """TokenData"""
    username: str
