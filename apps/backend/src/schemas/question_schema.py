from pydantic import BaseModel

class QuestionSchema(BaseModel):
    id: int
    lesson_id: int
    question: str
    options: list[str]
    correct_answer: int

class QuestionIdSchema(BaseModel):
    id: int