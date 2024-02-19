from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class QueryRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cadastral_number = db.Column(db.String(128), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    result = db.Column(db.Boolean)

    def to_dict(self):
        return {
            'id': self.id,
            'cadastral_number': self.cadastral_number,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'result': self.result
        }
