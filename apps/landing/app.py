from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    # Configuração para gerar estatico
    app.config['FREEZER_DESTINATION'] = 'build'
    app.config['FREEZER_RELATIVE_URLS'] = True

    CURSOS = [
        {
            "id": 1,
            "icon": "terminal",
            "title": "Python Fundamentos",
            "description": "Aprenda os conceitos essenciais da linguagem mais popular.",
            "total_lessons": 2,
            "color": "#306998",
            "rating": 4.8,
            "rating_count": 42,
        },
        {
            "id": 2,
            "icon": "flame",
            "title": "Flask API Masterclass",
            "description": "Crie APIs RESTful profissionais com documentacao automatica.",
            "total_lessons": 2,
            "color": "#FF5722",
            "rating": 4.6,
            "rating_count": 38,
        },
    ]

    FEATURES = [
        {"icon": "book-open", "title": "Cursos Interativos",
            "description": "Conteudo organizado em modulos progressivos."},
        {"icon": "lightbulb", "title": "Quizzes Praticos",
            "description": "Perguntas reais em cada licao."},
        {"icon": "bar-chart-3", "title": "Progresso Salvo",
            "description": "Historico persistente no banco."},
        {"icon": "refresh-cw", "title": "Refaca Licoes",
            "description": "Pratique quantas vezes quiser."},
        {"icon": "smartphone", "title": "Multiplataforma",
            "description": "Roda no navegador, desktop e mobile."},
        {"icon": "file-text", "title": "API Documentada",
            "description": "Swagger gerado automaticamente."},
    ]

    TECH_STACK = [
        {"name": "Flask", "role": "Backend & SSR", "icon": "flame"},
        {"name": "SQLAlchemy", "role": "ORM & Migrations", "icon": "database"},
        {"name": "PostgreSQL", "role": "Banco de Dados", "icon": "hard-drive"},
        {"name": "Flet", "role": "UI Multiplataforma", "icon": "smartphone"},
        {"name": "Tailwind CSS", "role": "Estilizacao", "icon": "palette"},
        {"name": "Docker", "role": "Containers", "icon": "container"},
    ]

    app.config['CURSOS'] = CURSOS

    @app.route('/')
    def index():
        return render_template('index.html', cursos=CURSOS, features=FEATURES, tech_stack=TECH_STACK)

    @app.route('/cursos/<int:curso_id>/')
    def curso_detalhe(curso_id):
        curso = next((c for c in CURSOS if c['id'] == curso_id), None)
        if not curso:
            return render_template('404.html'), 404
        return render_template('curso.html', curso=curso)

    @app.errorhandler(404)
    def pagina_nao_encontrada(e):
        return render_template('404.html'), 404

    return app


if __name__ == '__main__':
    app.run(debug=True, port=3000)
