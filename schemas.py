from pydantic import AliasPath, BaseModel, ConfigDict, Field


class DepartmentCreate(BaseModel):
    department_name: str


class DepartmentOut(DepartmentCreate):
    model_config = ConfigDict(from_attributes=True)

    department_id: int


class StudentCreate(BaseModel):
    student_name: str
    department_id: int


class StudentOut(StudentCreate):
    model_config = ConfigDict(from_attributes=True)

    student_id: int
    department_name: str = Field(
        validation_alias=AliasPath("department", "department_name")
    )