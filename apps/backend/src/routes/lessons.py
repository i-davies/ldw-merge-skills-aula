from flask import Blueprint, jsonify
from schemas.question_schema import QuestionIdSchema
from models import Lesson, Question

lessons_bp = Blueprint('lessons', __name__)


@lessons_bp.route('/<int:lesson_id>/questions', methods=['GET'])
def get_questions_by_lesson(lesson_id):
    """
    Lista IDs das perguntas de uma aula (para paginação)
    ---
    tags:
      - Aulas
    parameters:
      - name: lesson_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Lista de IDs de perguntas
        schema:
          type: array
          items:
            $ref: '#/definitions/QuestionId'
      404:
        description: Aula não encontrada
    """
    lesson = Lesson.query.get(lesson_id)
    if not lesson:
        return jsonify({"error": "Aula não encontrada"}), 404
    

    questions = Question.query.filter_by(lesson_id=lesson_id).order_by(Question.order).all()

    result = [QuestionIdSchema(id=q.id).model_dump() for q in questions]
    return jsonify(result)