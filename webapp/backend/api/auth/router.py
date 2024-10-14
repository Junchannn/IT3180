from fastapi import APIRouter, Depends, HTTPException, Response, status
from auth.schema import Register, ForgotPassword
from sqlalchemy.future import select
from utils.dbUtil import get_session, AsyncSession
from utils.cryptoUtil import hash_password, verify_password
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated
from utils.jwtUtil import create_access_token
from utils.models import Apartment
from auth.crud import find_exist_user
import uuid

router = APIRouter(prefix="/api/v1")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Register route
@router.post("/auth/register", response_model=Register)
async def register(reg: Register, 
                   db: AsyncSession = Depends(get_session)):
    
    # Check if the username already exists
    found_cred = await find_exist_user(reg, db=db)
    if found_cred:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    # Hash the password before saving it
    enc_password = hash_password(reg.password)
    reg.password = enc_password
    new_apartment = Apartment(**reg.dict())
    
    # Add to the database
    try:
        db.add(new_apartment)
        await db.commit()
        return {**reg.dict()}
    
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to register")

# Login route
@router.post("/auth/login")
async def login(response: Response, 
                form_data: Annotated[OAuth2PasswordRequestForm, Depends()], 
                db: AsyncSession = Depends(get_session)) -> dict:

    # Find user by username
    user = await db.scalar(select(Apartment).where(Apartment.username == form_data.username))
    if user is None or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    # Create access token
    access_token = create_access_token(
        data={"username": user.username},
    )
    response.set_cookie(key="Authorization", value=f"Bearer {access_token}", httponly=True)
    
    return {
        "access_token": access_token, 
        "token_type": "bearer"
    }

@router.post("/auth/forgot-password")
async def forgot_password(request: ForgotPassword):

    result = await find_exist_user(request.email)

    if not result:
        raise HTTPException(status_code=404, detail="User not found.")

    reset_code = str(uuid.uuid1())