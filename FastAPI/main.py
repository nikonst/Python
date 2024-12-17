from fastapi import FastAPI
from typing import List
from model import User, Gender, Role
from uuid import UUID, uuid4

app = FastAPI()

db: List[User] = [
    User( 
        id = UUID("781c30e6-157d-4819-a1bb-f7baa0419ee9"),
        firstName = "Joe",
        lastName = "Doe",
        gender = Gender.male,
        roles = [Role.admin]
        ),
    User( 
        id = UUID("b4623d6f-7441-4519-a50a-0951796b963e"),
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