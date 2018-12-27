# 登录相关的业务逻辑在此

from flask import Blueprint

passport_blu = Blueprint('passport',__name__,url_prefix='/passport')

from  . import views