from fastapi import FastAPI, HTTPException, Depends, Header, Request
from typing import List, Optional
from model import User, Author, userLogin, Gender, Role
from uuid import UUID, uuid4
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer

import json
import jwt
import secretKey

# Secret key to encode and decode the JWT token
SECRET_KEY = secretKey.secret_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Open the JSON file for AUTHORS
with open('data/authors.json') as f:
    authors = json.load(f)

dbAuthors: List[Author] = []

for person in authors:
    dbAuthors.append(
        Author( 
         id = person["id"],
         firstName = person["firstName"],
         lastName = person["lastName"],
         gender = person["gender"], # Gender.male,
         email = person["email"],
         books = person["books"]
         )
    )

# Open the JSON file for USERS
with open('data/users.json') as f:
    users = json.load(f)

dbUsers: List[User] = []

for u in users:
    dbUsers.append(
        User( 
         id = u["id"],
         username = u["username"],
         password = u["password"],
         firstName = u["firstName"],
         lastName = u["lastName"],
         gender = u["gender"],
         email = u["email"]
         )
    )

# Function to create a JWT token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    print(to_encode)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Dependency to get the current user from the token
# OAuth2 password flow
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return User(username=username)
    except jwt.PyJWTError:
        raise credentials_exception
    
# define APIs
app = FastAPI()

@app.post("/api/login")
async def userLogin(u: userLogin):
    for usr in dbUsers:
        if (u.username == usr.username):
            if (u.password == usr.password):
                access_token = create_access_token(data={"user": usr.username})
                return {"access_token": access_token, "token_type": "bearer"}
    return {"Msg":"User not found"}

@app.get("/api/login/token")
async def getToken(request: Request):
    my_auth = request.headers.get('Authorization')
    if not my_auth:
        raise HTTPException(status_code=401, detail="Unauthorized")
        #return {"No Auth":"No Auth Header"}
    try:
        payload = jwt.decode(my_auth[7:], SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        return {"200": "Valid token"}
    except:
        raise HTTPException(status_code=498, detail="Ivalid Token")
        #return {"Not OK": "Invalid token"}

@app.get("/")
async def root():
    return {"FastAPI":"Implementation"}

#Open api route
@app.get("/api/authors")
async def fetchAuthors():
    return dbAuthors

#Protected api route
@app.post("/api/authors")
async def addAuthor(a: Author, request: Request):
    print(request.headers.get('Authorization'))
    dbAuthors.append(a)
    return {"id":a.id}

#Protected api route
@app.delete("/api/authors/delete/{authorID}")
async def deleteAuthor(authorID: UUID):
    for a in dbAuthors:
        if a.id == authorID:
            dbAuthors.remove(a)
            return {"detail" : "Author removed"}
    raise HTTPException(
        status_code=404,
        detail=f"User with id {authorID} does not exist"
    )