from typing import Union, Tuple
from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from database import db
from models import Question, QuestionAttempt, LessonProgress, User
from schemas.progress_schema import (
    SubmitAnswerSchema,
    AnswerResultSchema,
    ResetProgressSchema,
    AttemptSchema,
    LessonProgressSchema,
    UserHistorySchema
)

progress_bp = Blueprint('progress', __name__)

@progress_bp.route('/', methods=['POST'])
def submit_answer() -> Union[Response, Tuple[Response, int]]:
    """
    Submete uma resposta e salva o progresso
    ---
    tags:
      - Progresso
    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/SubmitAnswer'
    responses:
      200:
        description: Resultado da submissão
        schema:
          $ref: '#/definitions/AnswerResult'
      400:
        description: Dados inválidos (erro de validação)
        schema:
          $ref: '#/definitions/Error'
      404:
        description: Pergunta não encontrada
        schema:
          $ref: '#/definitions/Error'
    """
    # Validação com Pydantic
    try:
        data = SubmitAnswerSchema(**request.json)
    except ValidationError as err:
        return jsonify({"errors": err.errors()}), 400

    user_id: int = data.user_id
    question_id: int = data.question_id
    selected_option: int = data.selected_option

    # Busca a pergunta no "Banco"
    question = Question.query.get(question_id)
    
    if not question:
        return jsonify({"error": "Pergunta não encontrada"}), 404
    
    # Verifica se o usuário existe
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error", "Usuário não encontrado"}), 404

    # Verifica a resposta
    is_correct = (selected_option == question.correct_answer)
    
    # Registra a tentativa no banco
    attempt = QuestionAttempt(
        user_id=user_id,
        question_id=question_id,
        selected_option=selected_option,
        is_correct=is_correct
    )
    db.session.add(attempt)
    db.session.commit()

    # Verificar se a lição foi concluída
    lesson_id = question.lesson_id
    lesson_questions = Question.query.filter_by(lesson_id=lesson_id).all()

    all_correct = True
    for q in lesson_questions:
        has_correct = QuestionAttempt.query.filter_by(
            user_id=user_id,
            question_id=q.id,
            is_correct=True
        ).first() is not None

        if not has_correct:
            all_correct = False
            break
        
    if all_correct:
      # Atualiza ou cria o registro de progresso da lição
      progress =  LessonProgress.query.filter_by(
          user_id=user_id, lesson_id=lesson_id
      ).first()

      if not progress:
          progress = LessonProgress(
              user_id=user_id,
              lesson_id=lesson_id,
              is_completed=True,
              completed_at=db.func.now(),
          )
          db.session.add(progress)
      else:
          if not progress.is_completed:
              progress.is_completed = True
              progress.completed_at = db.fun.now()
      db.session.commit()

    result = AnswerResultSchema(
        is_correct=is_correct,
        correct_answer=question.correct_answer,
        message="Resposta correta!" if is_correct else "Tente novamente."   
    ).model_dump()

    return jsonify(result)

@progress_bp.route('/history/<int:user_id>', methods=['GET'])
def get_history(user_id: int) -> Response:
    """
    Retorna o histórico completo do aluno
    ---
    tags:
      - Progresso
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID do usuário
    responses:
      200:
        description: Histórico do aluno
        schema:
          $ref: '#/definitions/UserHistory'
    """
    # Lições completadas
    completed = LessonProgress.query.filter_by(
        user_id=user_id, is_completed=True
    ).all()

    # Últimas 10 tentativas (mais recentes primeiro)
    recent = QuestionAttempt.query.filter_by(
        user_id=user_id
    ).order_by(QuestionAttempt.timestamp.desc()).limit(10).all()

    result = UserHistorySchema(
        user_id=user_id,
        completed_lessons=[p.to_dict() for p in completed],
        recent_attempts=[a.to_dict() for a in recent],
        total_score=len(completed),
    ).model_dump()

    return jsonify(result)