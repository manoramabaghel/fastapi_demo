from typing import List

from sqlalchemy.orm import Session  # type: ignore

from model.models import Item, User
from model.schemas import UserSchema


def get_item_by_name(session: Session, name: str) -> Item:
    return session.query(Item).filter(Item.name == name).first()


def get_items(session: Session, skip: int = 0, limit: int = 100) -> List[Item]:
    return session.query(Item).offset(skip).limit(limit).all()


def insert_user(session: Session, user_schema: UserSchema):
    # UserSchema()
    data  = session.query(User).filter(User.email == user_schema.email and User.password == user_schema.password).first()
    if data is None:
        user = User(user_schema.fullname, user_schema.email, user_schema.password)
        session.add(user)
        session.commit()
        print('insert data successfully')
        return True
    else:
        print('data is already exist')
        return False



def get_user(session: Session, user_schema: UserSchema) -> User:
    # UserSchema()

    # user = User(user_schema.fullname, user_schema.email, user_schema.password)
    # session.add(user)
    # session.commit()
    # print('insert data successfully')
    # return session.query(User).filter(User.email == user_schema.email and User.password == user_schema.password).first()
    return session.query(User).filter(User.email == user_schema.email , User.password == user_schema.password).first()
