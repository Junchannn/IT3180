from sqlalchemy.orm import (
    relationship,   
    mapped_column,
    Mapped,
    DeclarativeBase
)
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from datetime import datetime
class Base(AsyncAttrs, DeclarativeBase):
    pass

class Apartment(Base):
    __tablename__ = "apartment"
    
    room_no: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    mail: Mapped[str] = mapped_column(String, nullable=False)
    floor: Mapped[int] = mapped_column(Integer, nullable=False)
    room_member: Mapped[list["Member"]] = relationship("Member", back_populates="room")

class Member(Base):
    __tablename__ = "member"
    
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    gender: Mapped[bool] = mapped_column(Boolean, nullable=False)
    phonenumber: Mapped[str] = mapped_column(String, primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("apartment.room_no"), nullable=False)
    room: Mapped["Apartment"] = relationship("Apartment", back_populates="room_member")


class Code(Base):
    __tablename__ = "code"
    id: Mapped[int] = mapped_column(Integer, primary_key=True),
    mail: Mapped[str] = mapped_column(String, nullable=False)
    reset_code: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[bool] = mapped_column(bool, nullable=False)
    expired_in: Mapped[datetime] = mapped_column(DateTime)