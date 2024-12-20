from fastapi import FastAPI, HTTPException
from typing import List
from model import User, Gender, Role
from uuid import UUID, uuid4
from datetime import datetime, timedelta

import json
import jwt

import secretKey
# Secret key to encode and decode the JWT token
SECRET_KEY = secretKey.secret_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Open the JSON file
with open('data/authors.json') as f:
    data = json.load(f)

# Function to create a JWT token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

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
    return {"FastAPI":"Implementation"}

@app.get("/api/users")
async def fetchUsers():
    return db

@app.post("/api/users")
async def addUser(user: User):
    db.append(user)
    return {"id":user.id}

@app.delete("/api/users/delete/{userID}")
async def deleteUser(userID: UUID):
    for u in db:
        if u.id == userID:
            db.remove(u)
            return
    raise HTTPException(
        status_code=404,
        detail=f"User with id {userID} does not exist"
    )