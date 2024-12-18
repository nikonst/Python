from fastapi import FastAPI
from typing import List
from model import User, Gender, Role
from uuid import UUID, uuid4

import json

# Open the JSON file
with open('data/data.json') as f:
    data = json.load(f)

app = FastAPI()

db: List[User] = []

for person in data:
    db.append(
        User( 
         id = person["id"],
         firstName = person["firstName"],
         lastName = person["lastName"],
         gender = person["gender"], # Gender.male,
         email = person["email"],
         roles = person["roles"]
         )
    )

@app.get("/")
async def root():
    return {"Hello":"Everybody"}

@app.get("/api/users")
async def fetchUsers():
    return db

@app.post("/api/users")
async def addUser(user: User):
    print(user)
    db.append(user)
    return {"id":user.id}