"""
API route definitions for student CRUD operations and authentication endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.student import Student
from app.services import student_service
from app.auth_utils import create_access_token, get_password_hash, verify_password, get_current_user

router = APIRouter()

# Dummy user for demonstration
fake_user = {
    "username": "admin",
    "hashed_password": get_password_hash("admin123")
}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticate user and return a JWT access token.
    """
    if form_data.username != fake_user["username"] or not verify_password(form_data.password, fake_user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": fake_user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/students/{student_id}", dependencies=[Depends(get_current_user)])
def create_student(student_id: int, student: Student):
    """
    Create a new student with the given ID and student data.

    Args:
        student_id (int): The unique ID for the student.
        student (Student): The student data to add.

    Returns:
        dict: Success message and the added student data.
    """
    return student_service.create_student(student_id, student)

@router.get("/students/{student_id}", dependencies=[Depends(get_current_user)])
def read_student(student_id: int):
    """
    Retrieve a student by their ID.

    Args:
        student_id (int): The unique ID for the student.

    Returns:
        Student: The student data if found.
    """
    return student_service.read_student(student_id)

@router.put("/students/{student_id}", dependencies=[Depends(get_current_user)])
def update_student(student_id: int, student: Student):
    """
    Update an existing student's data by their ID.

    Args:
        student_id (int): The unique ID for the student.
        student (Student): The updated student data.

    Returns:
        dict: Success message and the updated student data.
    """
    return student_service.update_student(student_id, student)

@router.delete("/students/{student_id}", dependencies=[Depends(get_current_user)])
def delete_student(student_id: int):
    """
    Delete a student by their ID.

    Args:
        student_id (int): The unique ID for the student.

    Returns:
        dict: Success message after deletion.
    """
    return student_service.delete_student(student_id)

@router.get("/")
def root():
    """
    Root endpoint providing API information and available endpoints.

    Returns:
        dict: Information about available endpoints and authorship.
    """
    return {
        "endpoints": {
            "Create": "POST /students/{student_id}",
            "Read": "GET /students/{student_id}",
            "Update": "PUT /students/{student_id}",
            "Delete": "DELETE /students/{student_id}"
        },
        "author": "Chandrakant"
    }
