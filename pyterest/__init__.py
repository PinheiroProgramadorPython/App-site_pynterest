from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__, template_folder="templates")


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "cd4ca554a626be7a6e9aa6c057e3b140"
app.config["UPLOAD_FOLDER"] = "static/fotos-posts"

database = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "homepage"

bcrypt = Bcrypt(app)

from pyterest import routes
