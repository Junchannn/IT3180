from fastapi import APIRouter, Depends, HTTPException, Response, status
from auth.schema import Register, ForgotPassword
from sqlalchemy.future import select
from utils import dbUtil, cryptoUtil, jwtUtil, models, mailUtil
from auth import crud
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated
import uuid

router = APIRouter(prefix="/api/v1")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Register route
@router.post("/auth/register", response_model=Register)
async def register(reg: Register, 
                   db: dbUtil.AsyncSession = Depends(dbUtil.get_session)):
    
    # Check if the username already exists
    found_cred = await crud.find_exist_user(reg, db=db)
    if found_cred:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    # Hash the password before saving it
    enc_password = cryptoUtil.hash_password(reg.password)
    reg.password = enc_password
    new_models = models.Apartment(**reg.dict())
    
    # Add to the database
    try:
        db.add(new_models)
        await db.commit()
        return {**reg.dict()}
    
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to register")

# Login route
@router.post("/auth/login")
async def login(response: Response, 
                form_data: Annotated[OAuth2PasswordRequestForm, Depends()], 
                db: dbUtil.AsyncSession = Depends(dbUtil.get_session)) -> dict:

    # Find user by username
    user = await db.scalar(select(models.Apartment).where(models.Apartment.username == form_data.username))
    if user is None or not cryptoUtil.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    # Create access token
    access_token = jwtUtil.create_access_token(
        data={"username": user.username},
    )
    response.set_cookie(key="Authorization", value=f"Bearer {access_token}", httponly=True)
    
    return {
        "access_token": access_token, 
        "token_type": "bearer"
    }

@router.post("user/auth/forgot-password")
async def forgot_password(request: ForgotPassword,
                          db: dbUtil.AsyncSession = Depends(dbUtil.get_session)):

    result = await crud.find_exist_email(request, db=db)

    if not result:
        raise HTTPException(status_code=404, detail="User not found.")

    # Create reset code and save in database
    reset_code = str(uuid.uuid1())
    new_code = await crud.create_reset_code(request.mail, reset_code)
    print("[+] Code:",new_code)
    try:
        db.add(new_code)
        await db.commit()
    
    except Exception as e:
        await db.rollback()
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create reset code")
    
    subject = "Hello"
    recipient = [request.mail]
    reset_link = f"http://localhost/user/auth/forgot-password?reset_password_token={reset_code}"

    # Load HTML email template and replace placeholders
    html_body = mailUtil.load_html_template("template/forget_email.html", {"reset_link": reset_link})

    await mailUtil.send_email(subject, recipient, html_body)

    return {
        "code" : 200,
        "message": "Password reset email has been sent."
    }
