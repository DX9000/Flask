# current_app:应用上下文里的变量，表示当前url
from flask import current_app
from flask import render_template

from . import index_blu

@index_blu.route('/')
def index():
    # session['name'] = 'ITcast'
    # logging.debug('测试db')
    # logging.warning('测试wa')
    # logging.info('测试if')
    # logging.fatal('测试ft')
    # current_app.logger.error('测试current_app')
    # redis_store.set('name','itcast')


    return render_template('news/index.html')

@index_blu.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/favicon.ico')