from typing import List
from fastapi import (
    HTTPException, 
    Depends, 
    status, 
    APIRouter
)
from sqlalchemy.orm import Session
from uuid import UUID

from src.db import models, schemas
from src.db.database import get_db

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

@router.post("/post", response_model=List[schemas.CreatePost])
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@router.post(
    "/create", 
    status_code=status.HTTP_201_CREATED, 
    response_model=schemas.CreatePost
)
def create_posts(post: schemas.CreatePost, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get(
    "/{post_id}", 
    response_model=schemas.CreatePost
)
def get_post(post_id: UUID, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == str(post_id)).first()
    db.commit()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

# Get first 10 posts
@router.get(
    "/", 
    response_model=List[schemas.CreatePost]
)
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).limit(10).all()
    db.commit()
    return posts