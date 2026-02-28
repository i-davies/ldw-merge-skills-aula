from flask import Blueprint, jsonify

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
          type: object
          properties:
            id:
              type: integer
            lesson_id:
              type: integer
            question:
              type: string
            options:
              type: array
              items:
                type: string
            correct_option:
              type: integer
      404:
        description: Pergunta não encontrada
    """
    question = next((q for q in QUESTIONS_DB if q['id'] == question_id), None)
    if question:
        return jsonify(question)
    return jsonify({"error": "Questão não encontrada"}), 404