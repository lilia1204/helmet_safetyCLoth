from flask import jsonify

from db_init import db_init as db
from sqlalchemy.exc import IntegrityError

"""
检查POST请求的json格式的数据中是否包含所需的参数。
:param request: Flask请求对象
:param required_params: 所需参数的列表
:return: 缺失参数的列表。如果所有参数都存在，返回空列表。
"""


def check_missing_params(request, required_params):
    missing_params = [param for param in required_params if param not in request.json]
    if missing_params:
        return jsonify({'code': -100, 'message': 'missing_params:' + str(missing_params), 'data': {}})
    return missing_params


'''
函数功能：数据库中添加数据，该操作为原子操作，如果未能添加成功，则回滚，取消操作
参数：需要添加的数据，models中定义的类
返回：
    0：添加成功
    1：添加失败
'''


def add_model(mNewItem):
    try:
        db.session.add(mNewItem)
        db.session.commit()
        return 0
    except Exception as e:
        print('数据库添加出现错误:')
        print(e)
        db.session.rollback()
        return -1


"""
更新模型实例的工具函数。

:param model_instance: 要更新的SQLAlchemy模型实例
:param data: 包含要更新字段和值的字典
"""


def update_model(modelInstance, data):
    for key, value in data.items():
        if hasattr(modelInstance, key):
            setattr(modelInstance, key, value)
    try:
        db.session.commit()
        return 0
    except Exception as e:
        db.session.rollback()
        print("修改数据库内容出现错误：")
        print(e)
        return -1


"""
删除模型实例的工具函数。
:param model_instance: 要删除的SQLAlchemy模型实例
"""


def delete_model(model_instance):
    if model_instance:
        try:
            db.session.delete(model_instance)
            db.session.commit()
            print("删除成功")
            return 0
        except IntegrityError as ie:
            db.session.rollback()  # 回滚事务，以防止数据库进入不一致状态
            print(f"Integrity error occurred while deleting the instance: {ie}")
            return -1
        except Exception as e:
            db.session.rollback()  # 回滚事务，以防止数据库进入不一致状态
            # 记录错误日志或进行其他错误处理
            print(f"An error occurred while deleting the instance: {e}")
            return -1
    else:
        print("Model instance cannot be None")
        return -2
