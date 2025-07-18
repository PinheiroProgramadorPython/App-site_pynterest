from pyterest import app, database
from pyterest.models import Usuario, Foto



with app.app_context():
    database.drop_all()
    database.create_all()

