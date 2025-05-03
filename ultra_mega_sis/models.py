from enum import Enum
from typing import List

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class UserTypes(Enum):
    USER = "user"
    TEACHER = "teacher"


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    role: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(String(100))
    grades: Mapped[List["Grade"]] = relationship(back_populates="student")


class Grade(Base):
    __tablename__ = "grade"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    grade: Mapped[str] = mapped_column(String(2))
    student: Mapped["User"] = relationship(back_populates="grades")
