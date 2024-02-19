# app/routes.py
from flask import jsonify, request
from .models import db, QueryRecord
from .external_api_simulation import simulate_external_request

def configure_routes(app):


    @app.route('/')
    def home():
        return 'Добро пожаловать в мое Flask-приложение!'

    @app.route('/ping', methods=['GET'])
    def ping():
        return jsonify(message="Server is running!"), 200

    @app.route('/query', methods=['POST'])

    def handle_query():

        data = request.get_json()
        existing_record = QueryRecord.query.filter_by(cadastral_number=data['cadastral_number']).first()

        if existing_record:
            # Обработка случая, когда запись уже существует
            return jsonify(error="Record with this cadastral_number already exists"), 400

        new_record = QueryRecord(
            cadastral_number=data['cadastral_number'],
            latitude=data['latitude'],
            longitude=data['longitude']
        )
        db.session.add(new_record)
        db.session.commit()

        result = simulate_external_request()
        new_record.result = result
        db.session.commit()

        return jsonify(result=result), 201

    @app.route('/history', methods=['GET'])
    def get_history():
        cadastral_number = request.args.get('cadastral_number', None)
        if not cadastral_number:
            return jsonify({'error': 'Cadastral number is required'}), 400

        records = QueryRecord.query.filter_by(cadastral_number=cadastral_number).all()

        if records:
            return jsonify([record.to_dict() for record in records]), 200
        else:
            return jsonify({'message': 'No records found for this cadastral number'}), 404
