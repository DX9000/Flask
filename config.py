import logging

from redis import StrictRedis


class Config():
    DEBUG = True

    SECRET_KEY = 'ZRqSDpV4b6wIoHKfgJqp5T2xiq7Jmryz2ms2XIsc3O8V5I8OTCKaMQOphf2RJVbk'


    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/information27'
    # SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # session
    SESSION_TYPE = 'redis'
    # 开启session签名
    SESSION_USE_SIGNER = True
    # 指定session保存到redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    # 设置session会过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2

    # 设置日志等级
    LOG_LEVEL = logging.DEBUG

class DevelopermentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

    SQALCHEMY_DATABASES_URL = 'mysql://root:mysql@127.0.0.1:3306/information27'

    LOG_LEVEL = logging.WARNING


class TestConfig(Config):
    TESTING = True

config = {
    'developerment': DevelopermentConfig,
    'production': ProductionConfig,
    'test': TestConfig
}