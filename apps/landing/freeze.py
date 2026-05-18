from flask_frozen import Freezer
from app import  create_app
import os

app = create_app()
freezer = Freezer(app)


@freezer.register_generator
def curso_detalhe():
    for curso in app.config.get('CURSOS', []):
        yield {'curso_id': curso['id']}

@freezer.register_generator
def static():
    static_dir = os.path.join(app.root_path, 'static')
    for filename in os.listdir(static_dir):
        yield {'filename': filename}
        

if __name__ == '__main__':
    import warnings
    warnings.filterwarnings('ignore')

    freezer.freeze()
    print("Site estatico gerado em /build")