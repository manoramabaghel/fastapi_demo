from typing import List

from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session  # type: ignore
from queries import crud
from model import models
from database.database import SessionLocal, engine
from model.schemas import ItemBase
from model.schemas import UserSchema, UserLoginSchema
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT


models.Base.metadata.create_all(bind=engine)
itemrouter = APIRouter()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@itemrouter.get("/items/",  dependencies=[Depends(JWTBearer())], response_model=List[ItemBase])
def read_items(
        skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    items = crud.get_items(session=session, skip=skip, limit=limit)

    # token creation

    return [i.serialize for i in items]


@itemrouter.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...), session: Session = Depends(get_session)):
    resp = crud.insert_user(session=session, user_schema=user)
    if resp:
        return signJWT(user.email)
    else:
        return {"status": 'error', "message": 'User email %s already registered' % user.email}


@itemrouter.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...), session: Session = Depends(get_session)):
    if crud.get_user(session=session, user_schema=user):
        return signJWT(user.email)
    return {"status": 'error', "message": 'Login details are not correct'}