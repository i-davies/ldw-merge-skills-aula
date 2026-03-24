from typing import Optional
from pydantic import BaseModel, Field


class SubmitAnswerSchema(BaseModel):
    """
    Schema de ENTRADA (validação) para submissão de respostas.
    Diferente dos outros schemas, este valida dados que CHEGAM na API.
    """
    user_id: int
    question_id: int
    selected_option: int = Field(ge=0)  # ge = greater or equal (>=0)


class AnswerResultSchema(BaseModel):
    """
    Schema de SAÍDA para o resultado de uma submissão.
    """
    is_correct: bool
    correct_answer: int
    message: str


class ResetProgressSchema(BaseModel):
    """
    Schema de ENTRADA para resetar o progresso de uma lição.
    Permite ao aluno "refazer" uma lição do zero.
    """
    user_id: int
    lesson_id: int


class AttemptSchema(BaseModel):
    """
    Schema de SAÍDA para uma tentativa individual.
    """
    id: int
    user_id: int
    question_id: int
    selected_option: int
    is_correct: bool
    timestamp: Optional[str] = None


class LessonProgressSchema(BaseModel):
    """
    Schema de SAÍDA para o progresso de uma lição.
    """
    id: int
    user_id: int
    lesson_id: int
    is_completed: bool
    completed_at: Optional[str] = None


class UserHistorySchema(BaseModel):
    """
    Schema de SAÍDA para o histórico completo do aluno.
    """
    user_id: int
    completed_lessons: list[dict]
    recent_attempts: list[dict]
    total_score: int


class ProgressResponseSchema(BaseModel):
    """
    Schema de SAÍDA para o progresso do usuário (compatibilidade).
    """
    user_id: int
    completed_questions: list[int]
    total_score: int