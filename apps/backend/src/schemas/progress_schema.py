from pydantic import BaseModel, Field

class SubmitAnswerSchema(BaseModel):
    user_id: int
    question_id: int
    # ge = greater or equal (>=0) - Maior ou igual a 0
    selected_option: int = Field(ge=0)  

class ProgressResponseSchema(BaseModel):
    user_id: int
    completed_questions: list[int]
    total_score: int