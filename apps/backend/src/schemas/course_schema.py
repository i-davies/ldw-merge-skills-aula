from pydantic import BaseModel

class CourseSchema(BaseModel):
    id: int
    title: str
    description: str
    total_lessons: int
    active: bool = True