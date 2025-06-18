"""
Service functions for CRUD operations on student data (in-memory storage).
"""

from fastapi import HTTPException
from app.schemas.student import Student

# In-memory storage for students
db = {}

def create_student(student_id: int, student: Student):
    """
    Create a new student in the in-memory database.

    Args:
        student_id (int): The unique ID for the student.
        student (Student): The student data to add.

    Raises:
        HTTPException: If the student already exists.

    Returns:
        dict: Success message and the added student data.
    """
    if student_id in db:
        raise HTTPException(status_code=400, detail="Student already exists")
    db[student_id] = student
    return {"message": "Student added successfully", "student": student}

def read_student(student_id: int):
    """
    Retrieve a student from the in-memory database by ID.

    Args:
        student_id (int): The unique ID for the student.

    Raises:
        HTTPException: If the student is not found.

    Returns:
        Student: The student data.
    """
    if student_id not in db:
        raise HTTPException(status_code=404, detail="Student not found")
    return db[student_id]

def update_student(student_id: int, student: Student):
    """
    Update an existing student's data in the in-memory database.

    Args:
        student_id (int): The unique ID for the student.
        student (Student): The updated student data.

    Raises:
        HTTPException: If the student is not found.

    Returns:
        dict: Success message and the updated student data.
    """
    if student_id not in db:
        raise HTTPException(status_code=404, detail="Student not found")
    db[student_id] = student
    return {"message": "Student updated successfully", "student": student}

def delete_student(student_id: int):
    """
    Delete a student from the in-memory database by ID.

    Args:
        student_id (int): The unique ID for the student.

    Raises:
        HTTPException: If the student is not found.

    Returns:
        dict: Success message after deletion.
    """
    if student_id not in db:
        raise HTTPException(status_code=404, detail="Student not found")
    del db[student_id]
    return {"message": "Student deleted successfully"}
