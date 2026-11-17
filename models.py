from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Department(Base):
    __tablename__ = "departments"

    department_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    department_name: Mapped[str] = mapped_column(String, index=True)

    students: Mapped[list["Student"]] = relationship(back_populates="department")


class Student(Base):
    __tablename__ = "students"

    student_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    student_name: Mapped[str] = mapped_column(String, index=True)
    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.department_id"), index=True
    )

    department: Mapped[Department] = relationship(back_populates="students")