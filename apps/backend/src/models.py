from database import db
from sqlalchemy.dialects.postgresql import JSONB


class Course(db.Model):
    """Modelo SQLAlchemy para a tabela de Cursos."""

    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    icon = db.Column(db.String)
    color = db.Column(db.String)
    total_lessons = db.Column(db.Integer)

    # Relacionamento: um curso tem várias lições
    lessons = db.relationship('Lesson', backref='course', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'icon': self.icon,
            'color': self.color,
            'total_lessons': self.total_lessons,
        }


class Lesson(db.Model):
    """Modelo SQLAlchemy para a tabela de Aulas/Lições."""

    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    order = db.Column(db.Integer)

    # Relacionamento: uma lição tem várias perguntas
    questions = db.relationship('Question', backref='lesson', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'course_id': self.course_id,
            'title': self.title,
            'description': self.description,
            'order': self.order,
        }


class Question(db.Model):
    """Modelo SQLAlchemy para a tabela de Perguntas."""

    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), nullable=False)
    question = db.Column(db.String, nullable=False)
    code = db.Column(db.String)
    options = db.Column(JSONB)
    correct_answer = db.Column(db.Integer)
    order = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'lesson_id': self.lesson_id,
            'question': self.question,
            'code': self.code,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'order': self.order,
        }