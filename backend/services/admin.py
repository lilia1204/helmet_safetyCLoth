from flask import jsonify
from models.admin import Admin
from utils import utils


def register(sUerName, sPassword):
    # 查看传过来的数据合不合法
    if sUerName is None or sPassword is None:
        return jsonify({'code': -98, 'message': 'data error', 'data': {}})

    # 首先查看该用户名是否存在，存在则不能注册
    admin = Admin.query.filter_by(userName=sUerName).first()
    if admin is not None:
        return jsonify({'code': -1, 'message': 'userName exit', 'data': {}})

    # 插入数据库进行注册
    newAdmin = Admin(
        userName=sUerName,
        password=sPassword
    )
    if utils.add_model(newAdmin) == 0:
        return jsonify({'code': 0, 'message': 'success', 'data': {}})
    else:
        return jsonify({'code': -99, 'message': 'db error', 'data': {}})


def login(sUerName, sPassword):
    # 查看传过来的数据合不合法
    if sUerName is None or sPassword is None:
        return jsonify({'code': -98, 'message': 'data error', 'data': {}})

    # 查看用户是否存在
    admin = Admin.query.filter_by(userName=sUerName).first()
    if admin is None:
        return jsonify({'code': -1, 'message': 'user not exit', 'data': {}})

    # 查看密码是否正确
    adm_dict = admin.to_dict()
    if adm_dict['password'] != sPassword:
        return jsonify({'code': -2, 'message': 'wrong password', 'data': {}})

    return jsonify({'code': 0, 'message': 'success', 'data': {}})
