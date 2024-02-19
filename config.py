import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///default.db')
    # Отслеживание изменений объектов и отправка сигналов (требует дополнительной памяти и должно быть отключено, если не нужно)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
