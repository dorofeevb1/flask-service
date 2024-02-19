from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    from .models import db, QueryRecord
    admin = Admin(app, name='QueryAdmin', template_mode='bootstrap3')
    admin.add_view(ModelView(QueryRecord, db.session))
