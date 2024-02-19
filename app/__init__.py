from flask import Flask
from .models import db
from .external_api_simulation import simulate_external_request
from .routes import configure_routes
import os
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qwerty@localhost/flask_service'
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-secret-key')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    configure_routes(app)  # Вызываем функцию для регистрации маршрутов

    return app
