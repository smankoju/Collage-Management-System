from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models import Department
from schemas import DepartmentCreate, DepartmentOut


router = APIRouter(prefix="/api/departments", tags=["departments"])


@router.get("/", response_model=list[DepartmentOut])
def get_departments(db: Session = Depends(get_db)) -> list[Department]:
    return list(db.scalars(select(Department)).all())


@router.post("/", response_model=DepartmentOut, status_code=status.HTTP_201_CREATED)
def create_department(
    department_data: DepartmentCreate,
    db: Session = Depends(get_db),
) -> Department:
    department = Department(department_name=department_data.department_name)
    db.add(department)
    db.commit()
    db.refresh(department)
    return department