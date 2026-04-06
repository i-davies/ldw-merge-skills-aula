import os
import httpx

# URL do ambiente ou usa o padrão localhost
API_URL = os.environ.get("API_URL", "http://localhost:5000/api")

def _request_json(method: str, path: str, json_data: dict | None = None) -> dict | list:
    """Função auxiliar para fazer requisições e tratar erros."""
    try:
        response = httpx.request(
            method=method,
            url=f"{API_URL}{path}",
            json=json_data,
            timeout=5.0
        )
        response.raise_for_status()
        return response.json()
    except Exception as exc:
        print(f"Erro na API ({path}): {exc}")
        raise RuntimeError("Servidor Indisponível")

def get_courses() -> list[dict]:
    return _request_json("GET", "/courses/")

def get_lessons(course_id: int) -> list[dict]:
    return _request_json("GET", f"/courses/{course_id}/lessons")

def get_lesson_question_ids(lesson_id: int) -> list[int]:
    """Retorna apenas os IDs das perguntas da lição."""
    payload = _request_json("GET", f"/lessons/{lesson_id}/questions")
    return [int(item["id"]) for item in payload]

def get_question_details(question_id: int) -> dict:
    return _request_json("GET", f"/questions/{question_id}")

def submit_answer(user_id: int, question_id: int, selected_option: int) -> dict:
    return _request_json(
        "POST", 
        "/progress", 
        json_data={
            "user_id": user_id,
            "question_id": question_id,
            "selected_option": selected_option
        }
    )