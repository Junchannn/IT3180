from pydantic import BaseModel, Field

class Credential(BaseModel):
    mail: str = Field(..., example="Angay@gmail.com")
    password: str = Field(..., example="test")

class Register(BaseModel):
    username: str = Field(..., example="Minhngu")
    password: str = Field(..., example="test")
    mail: str = Field(..., example="Angay@gmail.com")
    floor: int
    room_no: int

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class ForgotPassword(BaseModel):
    mail: str = Field(..., example="example@example.com")

