from flask import Blueprint, jsonify
from routes.questions import QUESTIONS_DB

lessons_bp = Blueprint('lessons', __name__)

# Dados Mockados (Simulando Banco de Dados)
LESSONS_DB = [
    {"id": 1, "course_id": 1, "title": "Introdução ao Python", "order": 1},
    {"id": 2, "course_id": 1, "title": "Variáveis e Tipos", "order": 2},
    {"id": 3, "course_id": 2, "title": "Setup do Ambiente Flask", "order": 1},
    {"id": 4, "course_id": 2, "title": "Blueprints", "order": 2},
]



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
            type: object
            properties:
              id:
                type: integer
      404:
        description: Aula não encontrada
    """
    lesson = next((l for l in LESSONS_DB if l['id'] == lesson_id), None)
    if not lesson:
        return jsonify({"error": "Aula não encontrada"}), 404
        
    # List Comprehension (Compreensão de Lista)
    # Uma forma concisa de criar uma nova lista baseada em uma lista existente.
    # [expressão for item in iterável if condição]
    # Aqui, estamos filtrando as perguntas pelo 'lesson_id' e retornando 
    # apenas um dicionário contendo o 'id' de cada pergunta.
    questions = [{"id": q['id']} for q in QUESTIONS_DB if q['lesson_id'] == lesson_id]
    return jsonify(questions)