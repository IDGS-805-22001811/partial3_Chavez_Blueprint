from app import create_app
from app.extensions import db, bcrypt
from app.models import Alumno

app = create_app()

with app.app_context():
    if not Alumno.query.filter_by(username='admin').first():
        usuario = Alumno(
            nombre="Admin",
            apellido_paterno="Admin",
            apellido_materno="Admin",
            fecha_nacimiento="2000-01-01",
            grupo="A",
            username="admin",
            password=bcrypt.generate_password_hash("admin123").decode('utf-8')
        )
        db.session.add(usuario)
        db.session.commit()
        print("Usuario admin creado con éxito!")
    else:
        print("El usuario admin ya existe")