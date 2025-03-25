from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,DateField,PasswordField
from wtforms.validators import DataRequired

class AlumnoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido_paterno = StringField('Apellido Paterno', validators=[DataRequired()])
    apellido_materno = StringField('Apellido Materno', validators=[DataRequired()])
    fecha_nacimiento = DateField('Fecha de Nacimiento', validators=[DataRequired()])
    grupo = SelectField('Grupo', choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], validators=[DataRequired()])
    
class GrupoForm(FlaskForm):
    grupo = SelectField('Seleccionar Grupo', choices=[])
    submit = SubmitField('Ver Calificaciones')