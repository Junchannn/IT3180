from pydantic import BaseModel

class Credential(BaseModel):
    username: str
    password: str

class Register(BaseModel):
    username: str
    password: str
    mail: str
    floor: int
    room: int

class member(BaseModel):
    first_name: str
    last_name: str
    gender: str
    phonenumber: str
    room_id: int

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None