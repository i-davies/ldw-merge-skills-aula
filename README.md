# LDW Merge Skills

Projeto desenvolvido na disciplina de Laboratório de Desenvolvimento Web (LDW) da FATEC. Este projeto possui um foco didático, contendo comentários explicativos sobre conceitos de Python (como List Comprehension, Generator Expressions e Type Hints) diretamente no código das rotas.


## Estrutura do Projeto

O projeto segue uma arquitetura baseada em microsserviços (monorepo), onde temos:

- `apps/backend`: API RESTful desenvolvida com Flask
- `apps/frontend` (Futuro): Interface do usuário

## Como Rodar (Backend)

Necessário `uv` instalado.

1. Navegue até a pasta do backend:
   ```bash
   cd apps/backend
   ```

2. Instale as dependências:
   ```bash
   uv sync
   ```

3. Rode o servidor:
   - **Modo Desenvolvimento (Auto-reload):**
     ```bash
     uv run flask --app src/app run --debug
     ```
   - *Ou modo normal:*
     ```bash
     uv run flask --app src/app run
     ```
   - *Alternativa Python direto:*
     ```bash
     uv run python src/app.py
     ```

4. Acesse a documentação da API:
   - Swagger UI: http://localhost:5000/apidocs

## Endpoints da API (Mock)
A API implementa o modelo REST com os seguintes recursos principais:
- `/api/courses`: Lista de cursos
- `/api/courses/<id>`: Detalhes do curso
- `/api/courses/<id>/lessons`: Lista de aulas do curso
- `/api/lessons/<id>/questions`: Lista de perguntas atreladas à aula
- `/api/questions/<id>`: Detalhes de uma pergunta específica
- `/api/progress/` (POST): Submissão de progresso de um usuário
- `/api/progress/<user_id>` (GET): Detalhes do progresso do usuário

