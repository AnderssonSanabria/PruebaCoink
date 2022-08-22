from typing import Optional
from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: Optional[int]
    email: EmailStr
    fullname: str
    city: str

    class Config:
        orm_mode = True
