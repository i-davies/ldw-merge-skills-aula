from flask import Blueprint, jsonify, request
from routes.questions import QUESTIONS_DB
from pydantic import ValidationError
from schemas.progress_schema import SubmitAnswerSchema, ProgressResponseSchema

progress_bp = Blueprint('progress', __name__)

# Memória VOLÁTIL de Progresso (Simulando banco em memória)
# Estrutura: { "user_id": { "question_id": is_correct } } 
USER_PROGRESS = {}

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
    question = next((q for q in QUESTIONS_DB if q['id'] == question_id), None)
    
    if not question:
        return jsonify({"error": "Pergunta não encontrada"}), 404

    # Verifica a resposta
    is_correct = (selected_option == question['correct_option'])
    
    # Salva no "Banco em Memória"
    if user_id not in USER_PROGRESS:
        USER_PROGRESS[user_id] = {}
        
    if is_correct:
         USER_PROGRESS[user_id][question_id] = True

    return jsonify({
        "correct": is_correct,
        "message": "Resposta correta!" if is_correct else "Tente novamente."
    })