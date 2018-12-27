from flask import abort
from flask import current_app
from flask import make_response
from flask import request

from info import constants
from info import redis_store
from info.utils.captcha.captcha import captcha
from . import passport_blu


@passport_blu.route('/image_code')
def get_image_code():
    print(1)
    # args:取到url中？后面的参数
    image_Code_Id = request.args.get('imageCodeId',None)
    if not image_Code_Id:
        return abort(403)
    name, text,image = captcha.generate_captcha()
    try:
        redis_store.set('ImageCodeId' + image_Code_Id, text, constants.IMAGE_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.debug(e)
        abort(500)
    response = make_response(image)
    response.headers['Content-Type'] = 'image/jpg'

    return response
