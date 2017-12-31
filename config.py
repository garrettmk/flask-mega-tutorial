import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             'sqlite:///' + os.path.join(basedir, 'app.db'))
    MAIL_SERVER = os.environ.get('MAIL_SERVER', None)
    MAIL_PORT = os.environ.get('MAIL_PORT', 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', None) is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', None)
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', None)
    ADMINS = ['garrett@mail.com']

    POSTS_PER_PAGE = 3
