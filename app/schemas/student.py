"""
Student schema definition using Pydantic BaseModel.
"""

from pydantic import BaseModel


class Student(BaseModel):
    """
    Student model representing basic information about a student.
    """

    name: str
    Gender: str
    age: int
