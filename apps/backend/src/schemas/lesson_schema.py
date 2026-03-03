from pydantic import BaseModel

class LessonSchema(BaseModel):
    id: int
    course_id: int
    title: str
    order: int