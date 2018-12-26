from redis import StrictRedis


class Config():
    DEBUG = True

    SECRET_KEY = 'ZRqSDpV4b6wIoHKfgJqp5T2xiq7Jmryz2ms2XIsc3O8V5I8OTCKaMQOphf2RJVbk'

    SQLALCHEMY_DATABASES_URL = 'mysql:root@172.0.0.1/information27'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 3306

    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 846000 * 2