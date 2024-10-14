
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from secrets import token_hex
from pydantic import BaseSettings

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=token_hex(32))


# Database connection URL (adjust to your DB credentials)
# DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/dev"



class Settings(BaseSettings):
    DB_CONNECTION: str
    DB_HOST: str
    DB_PORT: str
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"