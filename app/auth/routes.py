from flask import render_template, redirect, url_for, flash,request
from flask_login import login_user, logout_user
from app.models import Alumno,db
from app.auth.forms import LoginForm
from app.extensions import bcrypt
from app.auth import auth_bp

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        alumno = Alumno.query.filter_by(username=form.username.data).first()
        
        if alumno and alumno.password == form.password.data:  # Temporal para desarrollo
            login_user(alumno)
            flash('Inicio de sesión exitoso', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.index'))
        
        flash('Usuario o contraseña incorrectos', 'danger')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Sesión cerrada', 'info')
    return redirect(url_for('auth.login'))

