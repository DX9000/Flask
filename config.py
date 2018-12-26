from redis import StrictRedis


class Config():
    DEBUG = True

    SECRET_KEY = 'ZRqSDpV4b6wIoHKfgJqp5T2xiq7Jmryz2ms2XIsc3O8V5I8OTCKaMQOphf2RJVbk'


    SQALCHEMY_DATABASES_URL = 'mysql:root@172.0.0.1:3306/infomation27'
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