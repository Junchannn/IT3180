
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from secrets import token_hex
from pydantic_settings import BaseSettings
from pydantic import EmailStr
from functools import lru_cache

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=token_hex(32))


# Database connection URL (adjust to your DB credentials)
# DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/dev"


class Settings(BaseSettings):
    # Database settings
    DB_CONNECTION: str
    DB_HOST: str
    DB_PORT: str
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str

    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: EmailStr
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_STARTTLS: bool  # Replacing MAIL_TLS
    MAIL_SSL_TLS: bool
    USE_CREDENTIALS: bool

    class Config:
        env_file = ".env"  # Load from the .env file
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
