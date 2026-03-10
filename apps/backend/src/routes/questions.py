from flask import Blueprint, jsonify
from schemas.question_schema import QuestionSchema 

questions_bp = Blueprint('questions', __name__)

# Banco de Perguntas (Mock)
QUESTIONS_DB = [
    {
        "id": 1,
        "lesson_id": 1,
        "question": "O que é Python?",
        "options": ["Um reptil", "Uma linguagem de programação", "Um editor de texto"],
        "correct_option": 1
    },
    {
        "id": 2,
        "lesson_id": 1,
        "question": "Qual comando imprime textos?",
        "options": ["echo()", "console.log()", "print()"],
        "correct_option": 2
    }
]



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
    question = next((q for q in QUESTIONS_DB if q['id'] == question_id), None)
    if question:
        result = QuestionSchema(**question).model_dump()
        return jsonify(result)
    return jsonify({"error": "Questão não encontrada"}), 404