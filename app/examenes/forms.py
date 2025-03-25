from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,DateField,PasswordField,TextAreaField
from wtforms.validators import DataRequired
    
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ExamenForm(FlaskForm):
    nombre = StringField('Nombre del Examen', validators=[DataRequired()])
    fecha = DateField('Fecha del Examen', format='%Y-%m-%d', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción')
    submit = SubmitField('Guardar Examen')

class PreguntaForm(FlaskForm):
    pregunta = StringField('Pregunta', validators=[DataRequired()])
    opcion_a = StringField('Opción A', validators=[DataRequired()])
    opcion_b = StringField('Opción B', validators=[DataRequired()])
    opcion_c = StringField('Opción C', validators=[DataRequired()])
    opcion_d = StringField('Opción D', validators=[DataRequired()])
    respuesta_correcta = StringField('Respuesta Correcta (A, B, C o D)', validators=[DataRequired()])
    submit = SubmitField('Agregar Pregunta')

class TuFormulario(FlaskForm):
    grupo = SelectField("Grupo", choices=[("A", "Grupo A"), ("B", "Grupo B")])  
    
class RealizarExamenForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido_paterno = StringField('Apellido Paterno', validators=[DataRequired()])
    submit = SubmitField('Buscar Alumno')