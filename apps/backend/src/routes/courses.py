from flask import Blueprint, jsonify
from routes.lessons import LESSONS_DB
from schemas.course_schema import CourseSchema
from schemas.lesson_schema import LessonSchema

courses_bp = Blueprint('courses', __name__)

# Dados Mockados (Simulando Banco de Dados)
COURSES_DB = [
    {
        "id": 1,
        "title": "Python Fundamentos",
        "description": "Aprenda o básico de Python",
        "total_lessons": 4,
        "active": True
    },
    {
        "id": 2,
        "title": "Flask API Masterclass",
        "description": "Crie APIs profissionais",
        "total_lessons": 10,
        "active": True
    }
]

@courses_bp.route('/', methods=['GET'])
def get_courses():
    """
    Lista todos os cursos disponíveis
    ---
    tags:
      - Cursos
    responses:
      200:
        description: Lista de cursos
        schema:
          type: array
          items:
            $ref: '#/definitions/Course'
    """
    result = [CourseSchema(**c).model_dump() for c in COURSES_DB]
    return jsonify(result)

@courses_bp.route('/<int:course_id>', methods=['GET'])
def get_course_by_id(course_id):
    """
    Obtém detalhes de um curso específico
    ---
    tags:
      - Cursos
    parameters:
      - name: course_id
        in: path
        type: integer
        required: true
        description: ID do curso
    responses:
      200:
        description: Detalhes do curso
        schema:
          $ref: '#/definitions/Course'
      404:
        description: Curso não encontrado
    """

    # Generator Expression (Expressão Geradora)
    # Cria um gerador que percorre a lista de cursos
    # e retorna apenas o curso com o id informado
    # next() é usado para obter o primeiro item do gerador
    # Se nenhum item for encontrado, retorna None (valor default)
    course = next((c for c in COURSES_DB if c['id'] == course_id), None)
    
    if course:
        result = CourseSchema(**course).model_dump()
        return jsonify(result)
    
    return jsonify({"error": "Curso não encontrado"}), 404

@courses_bp.route('/<int:course_id>/lessons', methods=['GET'])
def get_lessons_by_course(course_id):
    """
    Lista aulas de um curso específico
    ---
    tags:
      - Cursos
    parameters:
      - name: course_id
        in: path
        type: integer
        required: true
        description: ID do curso para buscar aulas
    responses:
      200:
        description: Lista de aulas do curso
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              title:
                type: string
              order:
                type: integer
      404:
        description: Curso não encontrado
    """
    course = next((c for c in COURSES_DB if c['id'] == course_id), None)
    if not course:
        return jsonify({"error": "Curso não encontrado"}), 404
        
    # Filtra as lições pelo ID do curso
    course_lessons = [l for l in LESSONS_DB if l['course_id'] == course_id]
    
    # Ordena pelo campo 'order'
    # O método sort percorre a lista e passa cada item (dicionário) para o 'key'.
    # Aqui, 'x' representa um item da lista, que tem o formato esperado:
    # { "id": 1, "course_id": 1, "title": "Introdução ao Python", "order": 1 }
    #
    # O 'lambda x: x["order"]' é uma função anônima curta equivalente a:
    # def get_order(item): return item["order"]
    # course_lessons.sort(key=get_order)
    course_lessons.sort(key=lambda x: x['order'])
    
    return jsonify(course_lessons)