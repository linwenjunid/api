from flask import Blueprint,g,jsonify
from ..auth.verify import auth
from ..auth.errors import bad_request

api=Blueprint('api',__name__)

@api.before_request
@auth.login_required
def before_request():
   """
   1.所有api蓝本下的请求都要经过认证
   2.非匿名用户留下脚印
   """
   if not g.current_user.is_anonymous:   
       g.current_user.ping()

@api.app_errorhandler(404)
def page_not_found(e):
    """重新定义了404错误的返回
    """
    return bad_request(e.code)

from . import demo
