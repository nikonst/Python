from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: int
    username: str
    password: str
    firstName: str
    lastName: str
    email: str
    gender: Gender

class userLogin(BaseModel):
    username: str
    password: str

class Author(BaseModel):
    id: Optional[UUID] = uuid4()
    firstName: str
    lastName: str
    gender: Gender
    email: str
    books: List[str]