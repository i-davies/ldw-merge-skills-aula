from flask import Flask
from flasgger import Swagger

def create_app():
    app = Flask(__name__)

    # Configuração do Swagger
    app.config['SWAGGER'] = {
        'title': 'LDW Merge Skills',
        'uiversion': 3,
        'description': 'Plataforma de aprendizado de habilidades de desenvolvimento web',
        'specs_route': '/apidocs/'
    }
    Swagger(app)

    # Espaço reservado para registrar Blueprints
     # Register Blueprints
    from routes.health import health_bp
    from routes.courses import courses_bp
    from routes.lessons import lessons_bp
    from routes.questions import questions_bp
    
    app.register_blueprint(health_bp, url_prefix='/api')
    app.register_blueprint(courses_bp, url_prefix='/api/courses')
    app.register_blueprint(lessons_bp, url_prefix='/api/lessons')
    app.register_blueprint(questions_bp, url_prefix='/api/questions')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)