from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mail import  Mail
from flask_pagedown import PageDown
from flask_misaka import Misaka

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

mail = Mail(app)

bootstrap = Bootstrap(app)

# for adding markdown input and output
pageDown = PageDown(app)
misaka = Misaka(app)


from app import routes, models