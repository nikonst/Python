from fastapi import FastAPI, HTTPException
from typing import List
from model import User, Author, Gender, Role
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
    authors = json.load(f)

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

db: List[Author] = []

for person in authors:
    db.append(
        Author( 
         id = person["id"],
         firstName = person["firstName"],
         lastName = person["lastName"],
         gender = person["gender"], # Gender.male,
         email = person["email"],
         books = person["books"]
         )
    )

@app.get("/")
async def root():
    return {"FastAPI":"Implementation"}

@app.get("/api/authors")
async def fetchAuthors():
    return db

@app.post("/api/authors")
async def addAuthor(user: User):
    db.append(user)
    return {"id":user.id}

@app.delete("/api/authors/delete/{authorID}")
async def deleteAuthor(authorID: UUID):
    for a in db:
        if a.id == authorID:
            db.remove(a)
            return
    raise HTTPException(
        status_code=404,
        detail=f"User with id {userID} does not exist"
    )