from flask import Flask, redirect, url_for
from config import DevelopmentConfig
from app.extensions import db, login_manager, csrf, bcrypt
def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    bcrypt.init_app(app)
    
    from app.main import main_bp
    app.register_blueprint(main_bp)
    # Configure login manager
    login_manager.login_view = 'auth.login'
    
    # Import blueprints
    from app.auth import auth_bp
    from app.alumnos import alumnos_bp
    from app.examenes import examenes_bp
    
    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(alumnos_bp, url_prefix='/alumnos')
    app.register_blueprint(examenes_bp, url_prefix='/examenes')
    
    # User loader configuration
    from app.models import Alumno
    
    @login_manager.user_loader
    def load_user(user_id):
        with app.app_context():
            return Alumno.query.get(int(user_id))
    
    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))
    
    return app