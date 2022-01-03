from typing import TypedDict

from sqlalchemy import Column, Integer, String  # type: ignore
from pydantic import BaseModel
from database.database import Base


class ItemDict(TypedDict):
    name: str
    price: int

class UserDict(TypedDict):
    name: str
    email: str
    password: str


class Item(Base):
    """
    Defines the items model
    """

    __tablename__ = "items"

    name = Column(String(255), primary_key=True)
    price = Column(Integer)

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"<Item {self.name}>"

    @property
    def serialize(self) -> ItemDict:
        """
        Return item in serializeable format
        """
        return {"name": self.name, "price": self.price}


class User(Base):
    """
    Defines the items model
    """

    __tablename__ = "users"

    name = Column(String(255))
    email = Column(String(255), primary_key=True)
    password = Column(String(255))

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self) -> str:
        return f"<User {self.name}>"

    @property
    def serialize(self) -> UserDict:
        """
        Return item in serializeable format
        """
        return {"name": self.name, "email": self.email, 'password': self.password}


