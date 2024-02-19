import json
from flask_testing import TestCase
from app import create_app, db
from app.models import QueryRecord

class TestAPI(TestCase):
    def create_app(self):
        # Конфигурация приложения для тестирования
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        # Создает чистую базу данных перед каждым тестом
        db.create_all()

    def tearDown(self):
        # Удаляет все записи из базы данных после каждого теста
        db.session.remove()
        db.drop_all()

    def test_query_endpoint(self):
        # Генерация уникального кадастрового номера для теста
        unique_cadastral_number = '223-456-789-unique'
        data = {
            'cadastral_number': unique_cadastral_number,
            'latitude': 25.7558,
            'longitude': 47.6173
        }
        response = self.client.post('/query', data=json.dumps(data), content_type='application/json')

        # Проверка статуса ответа
        self.assertEqual(response.status_code, 201, msg=response.data.decode())

        # Проверка содержимого ответа
        response_data = json.loads(response.data.decode())
        self.assertIn('result', response_data)
        self.assertTrue(isinstance(response_data['result'], bool))
    def test_history_endpoint(self):
        # Добавление тестовых данных
        record1 = QueryRecord(cadastral_number="12345", latitude=10.0, longitude=10.0, result=True)
        record2 = QueryRecord(cadastral_number="12345", latitude=20.0, longitude=20.0, result=False)
        db.session.add(record1)
        db.session.add(record2)
        db.session.commit()

        # Выполнение GET-запроса к эндпоинту /history
        response = self.client.get('/history?cadastral_number=12345')
        data = json.loads(response.data.decode())

        # Проверка статуса ответа и содержимого
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['cadastral_number'], "12345")
        self.assertEqual(data[1]['cadastral_number'], "12345")

if __name__ == '__main__':
    import unittest
    unittest.main()
