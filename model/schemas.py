from pydantic import BaseModel, Field, EmailStr


class ItemBase(BaseModel):
    name: str
    price: int



class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Manorama Baghel",
                "email": "manoramabaghel18@gmail.com",
                "password": "youruser_password"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "manoramabaghel18@gmail.com",
                "password": "youruser_password"
            }
        }