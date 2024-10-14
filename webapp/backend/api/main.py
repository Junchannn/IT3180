import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from secrets import token_hex
from auth import router as auth_router
# from utils.models import engine
import os

app = FastAPI()

# Use an environment variable for the session secret key
session_secret_key = os.getenv("SESSION_SECRET_KEY", token_hex(32))
app.add_middleware(SessionMiddleware, secret_key=session_secret_key)

app.include_router(auth_router.router, tags=["Auth"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
