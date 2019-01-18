from datetime import datetime

import random
import re
from flask import abort, jsonify
from flask import current_app
from flask import make_response
from flask import request
from flask import session

from info import constants, db
from info import redis_store
from info.models import User
from info.utils.captcha.captcha import captcha
from info.utils.response_code import RET
from . import passport_blu

@passport_blu.route('/login',methods = ['POST'])
def login():
    param_dict = request.json
    mobile = param_dict.get('mobile')
    passport = param_dict.get('passport')
    if not all([mobile, passport]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数不全')
    if not re.match('1[35678]\\d{9}', mobile):
        return jsonify(errno=RET.PARAMERR, errmsg='手机号码格式错误')
    try:
        user = User.query.filter(User.mobile == mobile).first()
    except Exception as e :
        current_app.logger.error(e)
        return jsonify(erron=RET.DBERR,ermsg='数据库错误')
    if not user:
        return jsonify(erron=RET.NODATA, ermsg='用户不存在')
    if not user.check_password(passport):
        return jsonify(erron=RET.PWDERR, ermsg='密码校验失败')
    session['user_id'] = user.id
    session['mobile'] = user.mobile
    session['nick_name'] = user.nick_name
    return jsonify(erron=RET.OK, ermsg='登陆成功')



@passport_blu.route('/register',methods=['POST'])
def register():
    param_dict = request.json
    mobile = param_dict.get('mobile')
    smscode = param_dict.get('smscode')
    password = param_dict.get('password')
    if not all([mobile,smscode,password]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数不全')
    if not re.match('1[35678]\\d{9}', mobile):
        return jsonify(errno=RET.PARAMERR, errmsg='手机号码格式错误')

    try:
        real_text = redis_store.get('SMS_'+ mobile)
    except Exception as e:
        current_app.logger.debug(e)
        return jsonify(errno=RET.DBERR, errmsg='数据库查询失败')
    if not real_text:
        return jsonify(errno=RET.NODATA, errmsg='验证码输过期')
    if real_text != smscode:
        return jsonify(errno=RET.DATAERR, errmsg='验证码输入错误')
    user = User()
    user.mobile = mobile
    user.nick_name = mobile
    user.last_login = datetime.now()
    user.password = password


    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        current_app.logger.debug(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg='数据保存失败1')
    #
    session['user_id'] = user.id
    session['mobile'] = user.mobile
    session['nick_name'] = user.nick_name




    return jsonify(errno=RET.OK,  errmsg='注册成功')


@passport_blu.route('/sms_code',methods=['POST'])
def send_sms_code():
    # params_dict = json.loads(request.data)
    params_dict = request.json
    mobile = params_dict.get('mobile')
    image_code =  params_dict.get('image_code')
    image_code_id =  params_dict.get('image_code_id')
    if not all([mobile,image_code,image_code_id]):
        # return jsonify(errno='4100',errmsg='参数不全')
        return jsonify(errno=RET.PARAMERR, errmsg='参数不全')
    if not re.match('1[35678]\\d{9}',mobile):
        return jsonify(errno=RET.PARAMERR, errmsg='手机号码格式错误')
    try:
        real_image_code = redis_store.get('ImageCodeId' + image_code_id)
    except Exception as e:
        current_app.logger.debug(e)
        return jsonify(errno=RET.DBERR, errmsg='数据库查询失败')

    if not real_image_code:
        return jsonify(errno=RET.NODATA, errmsg='图片验证码过期')

    if real_image_code.lower() != image_code.lower():
        return jsonify(errno=RET.DATAERR, errmsg='验证码输入错误')

    sms_code_str =  random.randint(0,999999)
    current_app.logger.debug('短信验证码是：%06d' % sms_code_str)
    # resule = CCP().send_template_sms(mobile,['%06d' % sms_code_str, constants.SMS_CODE_REDIS_EXPIRES/5],3)

    # if resule != 0:
    #     # print(101)
    #     return jsonify(errno=RET.THIRDERR, errmsg='短信发送错误')
    try:
        redis_store.set('SMS_' + mobile, sms_code_str, constants.SMS_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.debug(e)
        print('数据保存失败')
        return jsonify(errno=RET.DBERR, errmsg='数据保存失败2')

    return jsonify(errno=RET.OK,errmsg='发送成功')





@passport_blu.route('/image_code')
def get_image_code():
    print(1)
    # args:取到url中？后面的参数
    image_Code_Id = request.args.get('imageCodeId',None)
    if not image_Code_Id:
        return abort(403)
    name, text,image = captcha.generate_captcha()
    print(text)
    try:
        redis_store.set('ImageCodeId' + image_Code_Id, text, constants.IMAGE_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.debug(e)
        abort(500)
    response = make_response(image)
    response.headers['Content-Type'] = 'image/jpg'

    return response
