from config import (
    app, 
    get_session,
    AsyncSession
)
from werkzeug.security import (
    generate_password_hash, 
    check_password_hash
)
from sqlalchemy.future import select
from sqlalchemy import or_
from datetime import timedelta
from database import Apartment, Member
from fastapi import (
    Depends, 
    HTTPException, 
    status, 
    Request,
    Response
)

from jwt.exceptions import InvalidTokenError
from model import *
from typing import Annotated, List
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm
)
import jwt
from security import *

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
@app.post("/register")
async def register(reg: Register, db: AsyncSession = Depends(get_session)):
    username = reg.username
    mail = reg.mail
    password = reg.password
    floor = reg.floor
    room = reg.room
    # Check if the username or password already exists
    found_cred = await db.scalar(
        select(Apartment).where(
            or_(Apartment.username == username, Apartment.password == generate_password_hash(password))
        )
    )
    if found_cred:
        raise HTTPException(status_code=400, detail="Username or password already exists")
    
    # Hash the password before storing it

    
    # Create a new Apartment object
    new_apartment = Apartment(room_no=room,
                              username=username,                         
                              password=generate_password_hash(password), 
                              mail=mail, 
                              floor=floor
                              )
    # Add and commit to the database
    try:
        db.add(new_apartment)
        await db.commit()  # Ensure this is awaited in async SQLAlchemy
        return {"message": "Register success"}, 200
    except Exception as e:
        await db.rollback()  # Rollback in case of any exception
        raise HTTPException(status_code=500, detail="Failed to register")
    


@app.post("/login")
async def login(response: Response, 
                form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                db : AsyncSession = Depends(get_session)
            ) -> Token:

    user = await db.scalar(select(Apartment).where(
        Apartment.username==form_data.username)
    )
    if user is None:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if check_password_hash(user.password, form_data.password):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"username": user.username}, expires_delta=access_token_expires
        )
        return Token(access_token=access_token, token_type="bearer")
        
    # if role == 'admin':
    #     return render_template("login_admin.html")
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

@app.get("/users/me")
async def user(request: Request, 
               token: Annotated[str, Depends(oauth2_scheme)],
               db : AsyncSession = Depends(get_session),
                ):
    print(token)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    if not username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not logged in")
    user = await db.scalar(select(Apartment).where(Apartment.username==username))
    room = user.room_no
    result = await db.scalars(select(Member).where(Member.room_id == room))
    members = result.fetchall()
    if not members:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No members found for the room")
    return members

        
@app.post("/user/me/add_member")
async def add_member(reg : member, 
                     token: Annotated[str, Depends(oauth2_scheme)],
                     db : AsyncSession = Depends(get_session)):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    user = await db.scalar(select(Apartment).where(Apartment.username==username))
    room_id = user.room_no
    first_name = reg.first_name
    last_name = reg.last_name
    gender = True if reg.gender == "Male" else False
    phonenumber = reg.phonenumber

    user = await db.scalar(select(Member).where(Apartment.username==username))
    if not username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not logged in")

    new_members = Member(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        phonenumber=phonenumber,
        room_id=room_id
    )
    try:
        db.add(new_members)
        await db.commit()  # Ensure this is awaited in async SQLAlchemy
        return {"message": "Register success"}, 200
    except Exception as e:
        await db.rollback()  # Rollback in case of any exception
        raise HTTPException(status_code=500, detail="Failed to add new member")
