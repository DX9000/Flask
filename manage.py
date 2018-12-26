from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


class Config():
    DEBUG = True

    SQALCHEMY_DATABASES_URL = 'mysql:root@172.0.0.1:3306/infomation27'
    SQLALCHEMY_TRACK_MODIFICATIONS = Flask

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route('/')
def index():
    return '00'

if __name__ == '__main__':
    app.run()