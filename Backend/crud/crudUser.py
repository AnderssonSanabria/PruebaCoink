from sqlalchemy.orm import Session
from models import User
from schemas import UserSchema


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_fullname(db: Session, fullname: str):
    return db.query(User).filter(User.fullname == fullname).first()


def get_users_by_city(db: Session, city: str, skip: int = 0, limit: int = 10000):
    return db.query(User).filter(User.city == city)


def get_users(db: Session, skip: int = 0, limit: int = 10000):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserSchema):
    db_user = User(email=user.email,
                   fullname=user.fullname,
                   city=user.city)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
