from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from app.alumnos import alumnos_bp  # Importa el blueprint desde el paquete actual
from app.models import Alumno, db
from app.auth.forms import AlumnoForm

@alumnos_bp.route('/alumno', methods=['GET', 'POST'])
def alumno():
    form = AlumnoForm()
    if form.validate_on_submit():
        from app.extensions import bcrypt
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        nuevo_alumno = Alumno(
            nombre=form.nombre.data,
            apellido_paterno=form.apellido_paterno.data,
            apellido_materno=form.apellido_materno.data,
            fecha_nacimiento=form.fecha_nacimiento.data,
            grupo=form.grupo.data,
            username=form.username.data,
            password=hashed_password
        )
        
        db.session.add(nuevo_alumno)
        try:
            db.session.commit()
            flash('Alumno registrado exitosamente', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error al registrar alumno: {str(e)}', 'danger')
            
        return redirect(url_for('alumnos.alumno'))
    
    return render_template('alumnos/alumno.html', form=form)