from info import redis_store
from . import index_blu

@index_blu.route('/')
def index():
    # session['name'] = 'ITcast'
    # logging.debug('测试db')
    # logging.warning('测试wa')
    # logging.info('测试if')
    # logging.fatal('测试ft')
    # current_app.logger.error('测试current_app')
    redis_store.set('name','itcast')
    return '00'