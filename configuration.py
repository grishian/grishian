import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfiguration():
    DEBUG = True
    SECRET_KEY = 'super secret key'
    SESSION_TYPE = 'memcached'


    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')

    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class PyConfiguration(BaseConfiguration):
    DEBUG_TB_ENABLED = False

