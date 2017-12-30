import os
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'


from app import routes, models, errors


if not app.debug:

    if not os.path.exists('logs'):
        os.mkdir('logs')

    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(
        logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        )
    )

    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

    mail_server = app.config['MAIL_SERVER']
    if mail_server:
        mail_port = app.config['MAIL_PORT']
        mail_username = app.config['MAIL_USERNAME']
        mail_password = app.config['MAIL_PASSWORD']

        host = (mail_server, mail_port)
        auth = (mail_username, mail_password) if mail_username or mail_password else None
        secure = () if app.config['MAIL_USE_TLS'] else None

        mail_handler = SMTPHandler(
            mailhost=host,
            fromaddr='no-reply@' + mail_server,
            toaddrs=app.config['ADMINS'],
            subject='Microblog Failure',
            credentials=auth,
            secure=secure
        )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)