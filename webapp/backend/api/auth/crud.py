from auth.schema import Register, ForgotPassword
from utils.dbUtil import get_session, AsyncSession
from utils import models
from fastapi import Depends
from sqlalchemy.future import select
from sqlalchemy import or_
from utils.cryptoUtil import hash_password
from datetime import datetime, timezone

async def find_exist_user(reg: Register, 
                          db: AsyncSession = Depends(get_session)):
    # Check if the user exists by username or password
    result = await db.scalar(
        select(models.Apartment).where(
            or_(models.Apartment.username == reg.username, models.Apartment.password == hash_password(reg.password))
        )
    )
    
    if result:
        return result
    return None  # Return None if the user does not exist

async def find_exist_email(forget: ForgotPassword, 
                          db: AsyncSession = Depends(get_session)):
    # Check if the user exists by username or password
    result = await db.scalar(
        select(models.Apartment).where(
            (models.Apartment.mail == forget.mail)
        )
    )
    
    if result:
        return result
    return None  # Return None if the user does not exist

async def create_reset_code(email: str, 
                            reset_code: str, 
                            ):
    
    expired_in_time = datetime.now(timezone.utc)
    expired_in_time_naive = expired_in_time.replace(tzinfo=None)
    new_code = models.Code(
        mail=email,
        reset_code=reset_code,
        status=True,
        expired_in=expired_in_time_naive
    )
    
    # Add to the database
    return new_code

