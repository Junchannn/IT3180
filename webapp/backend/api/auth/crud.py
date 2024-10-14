from auth.schema import Register
from utils.dbUtil import get_session, AsyncSession
from utils.models import Apartment
from fastapi import Depends
from sqlalchemy.future import select
from sqlalchemy import or_
from utils.cryptoUtil import hash_password

async def find_exist_user(reg: Register, db: AsyncSession = Depends(get_session)):
    # Check if the user exists by username or password
    result = await db.scalar(
        select(Apartment).where(
            or_(Apartment.username == reg.username, Apartment.password == hash_password(reg.password))
        )
    )
    
    if result:
        return result
    return None  # Return None if the user does not exist
