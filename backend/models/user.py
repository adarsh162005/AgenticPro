from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: str
    email: EmailStr
    display_name: str
    role: str = "student"
