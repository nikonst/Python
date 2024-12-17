from fastapi import FastAPI
from typing import List
from model import User, Gender, Role
from uuid import UUID, uuid4

app = FastAPI()

db: List[User] = [
    User( 
        id = uuid4(),
        firstName = "Joe",
        lastName = "Doe",
        gender = Gender.male,
        roles = [Role.admin]
        ),
    User( 
        id = uuid4(),
        firstName = "Mary",
        lastName = "Lawson",
        gender = Gender.female,
        roles = [Role.user]
        ),
]

@app.get("/")
async def root():
    return {"Hello":"Everybody"}

@app.get("/api/users")
async def fetchUsers():
    return db