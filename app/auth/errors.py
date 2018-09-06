from flask import jsonify

def unauthorized(message):
    response = jsonify({'error': '未授权', 'message': message})
    response.status_code = 401
    return response

def forbidden(message):
    response = jsonify({'error': '禁止访问', 'message': message})
    response.status_code = 403
    return response

def bad_request(message):
    response = jsonify({'error': '错误请求', 'message': message})
    response.status_code = 400
    return response

