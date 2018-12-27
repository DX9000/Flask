import logging

from redis import StrictRedis


class Config():
    DEBUG = True

    LOG_LEVEL = logging.DEBUG

    SECRET_KEY = 'ZRqSDpV4b6wIoHKfgJqp5T2xiq7Jmryz2ms2XIsc3O8V5I8OTCKaMQOphf2RJVbk'

    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/information28'
    # SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information27"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 846000 * 2

# class Developerment(Config):
#     DEBUG = False
#
#
#
# config = {
#     'developerment':Developerment,
#     'config':Config
# }
class DevelopermentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

    SQALCHEMY_DATABASES_URL = 'mysql//:root:mysql@127.0.0.1:3306/information28'

    LOG_LEVEL = logging.WARNING


class TestConfig(Config):
    TESTING = True

config = {
    'developerment': DevelopermentConfig,
    'production':ProductionConfig,
    'test':TestConfig
}