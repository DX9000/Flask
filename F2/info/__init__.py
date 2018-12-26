from flask import Flask
from flask.ext.session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis

from config import Config

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)

Session(app)

CSRFProtect(app)