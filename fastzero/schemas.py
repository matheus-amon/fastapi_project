from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserSchema(UserResponse):
    password: str


class UserList(BaseModel):
    users: list[UserResponse]
