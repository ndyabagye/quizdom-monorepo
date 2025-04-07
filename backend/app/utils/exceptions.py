"""Common Exceptions in the app"""
from fastapi import HTTPException, status

def raise_unauthorized(detail: str):
    """Unauthorised due to password, or session expiration"""
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
        headers={"WWW-Authenticate": "Bearer"}
    )
