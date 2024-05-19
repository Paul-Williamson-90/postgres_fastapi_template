from fastapi import FastAPI
import psycopg2

from src.db import models
from src.db.database import engine
from src.router.posts import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)

@app.get("/ping/")
async def ping():
    return {"message": "pong"}