from flask_httpauth import HTTPBasicAuth
from flask import g,jsonify
from ..models.user import User,AnonymousUser
from .errors import unauthorized

auth=HTTPBasicAuth()

@auth.verify_password
def verify_password(username,password):
    if username=='':
        g.current_user=AnonymousUser()
        return True
    user=User.query.filter_by(username=username).first()
    if not user:
        return False
    g.current_user=user
    return user.verify_password(password)

@auth.error_handler
def auth_error():
    return unauthorized('用户认证失败！')


