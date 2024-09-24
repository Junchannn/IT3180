import asyncio
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.middleware.sessions import SessionMiddleware
from secrets import token_hex

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=token_hex(32))

# Database connection URL (adjust to your DB credentials)
DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/dev"

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Session maker for async sessions
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency to get the async session

async def get_session() -> AsyncSession:
    async with async_session() as session:
        print("Connect to database")
        yield session  # Ensure it yields the AsyncSession



