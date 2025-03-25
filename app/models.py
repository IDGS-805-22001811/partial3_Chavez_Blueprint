from app.extensions import db
from flask_login import UserMixin

class Alumno(UserMixin, db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido_paterno = db.Column(db.String(50), nullable=False)
    apellido_materno = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.String(10), nullable=False)
    grupo = db.Column(db.String(10), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Alumno {self.username}>'

class Pregunta(db.Model):
    __tablename__ = 'preguntas'
    id = db.Column(db.Integer, primary_key=True)
    pregunta = db.Column(db.String(255), nullable=False)
    opcion_a = db.Column(db.String(50), nullable=False)
    opcion_b = db.Column(db.String(50), nullable=False)
    opcion_c = db.Column(db.String(50), nullable=False)
    opcion_d = db.Column(db.String(50), nullable=False)
    respuesta_correcta = db.Column(db.String(1), nullable=False)

class Respuesta(db.Model):
    __tablename__ = 'respuestas'
    id = db.Column(db.Integer, primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'))
    pregunta_id = db.Column(db.Integer, db.ForeignKey('preguntas.id'))
    respuesta_alumno = db.Column(db.String(1))
    
class Examen(db.Model):
    __tablename__ = 'examenes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    grupo = db.Column(db.String(10), nullable=False)  # Agregar esta línea

    def __repr__(self):
        return f'<Examen {self.nombre}>'
