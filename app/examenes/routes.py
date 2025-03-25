from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from . import examenes_bp
from .forms import ExamenForm, PreguntaForm  # Importa ambos formularios
from app.models import Examen, Pregunta, db,Alumno,Respuesta
from app.examenes.forms import RealizarExamenForm , TuFormulario # Importa el formulario

@examenes_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear():
    form_examen = ExamenForm()
    form_pregunta = PreguntaForm()

    if form_examen.validate_on_submit():
        examen = Examen(
            nombre=form_examen.nombre.data,
            fecha=form_examen.fecha.data,
            descripcion=form_examen.descripcion.data
        )
        db.session.add(examen)
        db.session.flush()  # Obtener ID antes del commit

        if form_pregunta.validate_on_submit():
            pregunta = Pregunta(
                examen_id=examen.id,
                pregunta=form_pregunta.pregunta.data,
                opcion_a=form_pregunta.opcion_a.data,
                opcion_b=form_pregunta.opcion_b.data,
                opcion_c=form_pregunta.opcion_c.data,
                opcion_d=form_pregunta.opcion_d.data,
                respuesta_correcta=form_pregunta.respuesta_correcta.data
            )
            db.session.add(pregunta)

        db.session.commit()
        flash('Examen y pregunta creados exitosamente!', 'success')
        return redirect(url_for('examenes.crear'))

    return render_template('examenes/crear.html', form_examen=form_examen, form_pregunta=form_pregunta)

from flask import request

@examenes_bp.route('/realizar', methods=['GET', 'POST'])
@login_required
def realizar():
    form = RealizarExamenForm()
    alumno = None
    preguntas = []
    mensaje_error = None

    if request.method == 'POST':
        if 'buscar_alumno' in request.form:
            # Buscar al alumno en la base de datos
            nombre = form.nombre.data
            apellido_paterno = form.apellido_paterno.data
            alumno = Alumno.query.filter_by(nombre=nombre, apellido_paterno=apellido_paterno).first()

            if alumno:
                preguntas = Pregunta.query.join(Examen).filter(Examen.grupo == alumno.grupo).all()
            else:
                mensaje_error = "Alumno no encontrado."

        elif 'guardar_examen' in request.form:
            alumno_id = request.form.get('alumno_id')
            alumno = Alumno.query.get(alumno_id)

            if alumno:
                preguntas = Pregunta.query.join(Examen).filter(Examen.grupo == alumno.grupo).all()
                for pregunta in preguntas:
                    respuesta_seleccionada = request.form.get(f'pregunta_{pregunta.id}')
                    respuesta_correcta = respuesta_seleccionada == pregunta.respuesta_correcta

                    respuesta = Respuesta(
                        alumno_id=alumno.id,
                        pregunta_id=pregunta.id,
                        respuesta_seleccionada=respuesta_seleccionada,
                        correcta=respuesta_correcta
                    )
                    db.session.add(respuesta)

                db.session.commit()
                flash('Examen guardado correctamente', 'success')
                return redirect(url_for('examenes.realizar'))

    return render_template('examenes/realizar.html', form=form, alumno=alumno, preguntas=preguntas, mensaje_error=mensaje_error)

@examenes_bp.route('/calificaciones', methods=['GET', 'POST'])
@login_required
def calificaciones():
    form = TuFormulario()
    calificaciones = []
    grupo_seleccionado = None

    if form.validate_on_submit():
        grupo_seleccionado = form.grupo.data
        calificaciones = (
            db.session.query(Alumno.nombre, Alumno.apellido_paterno, Pregunta.pregunta, Respuesta.respuesta_seleccionada, Respuesta.correcta)
            .join(Respuesta, Alumno.id == Respuesta.alumno_id)
            .join(Pregunta, Pregunta.id == Respuesta.pregunta_id)
            .filter(Alumno.grupo == grupo_seleccionado)
            .all()
        )

    return render_template('examenes/calificaciones.html', form=form, calificaciones=calificaciones, grupo_seleccionado=grupo_seleccionado)
