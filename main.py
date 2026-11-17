from fastapi import FastAPI

import models
from database import Base, engine
from routers import departments, students


Base.metadata.create_all(bind=engine)

app = FastAPI(title="College Management System API")
app.include_router(departments.router)
app.include_router(students.router)


@app.get("/")
def get_status() -> dict[str, str]:
    return {"status": "College Management System API is running"}