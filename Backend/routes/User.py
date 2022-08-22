from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from crud import crudUser
from models import Base
from schemas import UserSchema
from config import SessionLocal, engine

Base.metadata.create_all(bind=engine)
userRouter = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@userRouter.post("/users/", response_model=UserSchema)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    db_user = crudUser.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crudUser.create_user(db=db, user=user)


@userRouter.get("/users/", response_model=List[UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crudUser.get_users(db, skip=skip, limit=limit)
    return users


@userRouter.get("/users/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crudUser.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
