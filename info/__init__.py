from flask import Flask
from flask.ext.session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis

from config import config

db = SQLAlchemy()
def creat_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    # Flask很多拓展里都可以先初始化拓展对象，再init_app方法去初始化
    db.init_app(app)

    redis_store = StrictRedis(host=config[config_name].REDIS_HOST,port=config[config_name].REDIS_PORT)

    CSRFProtect(app)

    Session(app)

    return app