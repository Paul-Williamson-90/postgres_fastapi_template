from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class PostBase(BaseModel):
    id: UUID
    content: str
    title: str
    published: bool
    created_at: datetime

    class Config:
        orm_mode = True

class CreatePost(PostBase):
    class Config:
        orm_mode = True