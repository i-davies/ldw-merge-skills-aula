from flask import Blueprint, jsonify
from schemas.question_schema import QuestionSchema 
from models import Question

questions_bp = Blueprint('questions', __name__)

@questions_bp.route('/', methods=['GET'])
def get_all_questions() -> Response:
    """
    Lista todas as perguntas disponíveis
    ---
    tags:
      - Perguntas
    responses:
      200:
        description: Lista de todas as perguntas
        schema:
          type: array
          items:
            $ref: '#/definitions/Question'
    """
    questions = Question.query.all()
    result = [QuestionSchema(**q.to_dict()).model_dump() for q in questions]
    return jsonify(result)

@questions_bp.route('/<int:question_id>', methods=['GET'])
def get_question_details(question_id: int):
    """
    Obtém detalhes de uma pergunta
    ---
    tags:
      - Perguntas
    parameters:
      - name: question_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Detalhes da pergunta
        schema:
          $ref: '#/definitions/Question'
      404:
        description: Pergunta não encontrada
    """
    question = Question.query.get(question_id)
    if question:
        result = QuestionSchema(**question.to_dict()).model_dump()
        return jsonify(result)
    return jsonify({"error": "Questão não encontrada"}), 404