"""This is the beginning of execution"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers.auth_routers import router as auth_router
from app.routers.user_routers import router as user_router
from app.routers.quiz_routers import router as quiz_router
from app.routers.question_routers import router as question_router
from app.routers.answer_routers import router as answer_router
from app.utils.database import init_db

@asynccontextmanager
async def lifespan(_: FastAPI):
    """Using this to initialise database"""
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(quiz_router)
app.include_router(question_router)
app.include_router(answer_router)

@app.get("/")
def read_root():
    "Default route"
    return "Hello World"
