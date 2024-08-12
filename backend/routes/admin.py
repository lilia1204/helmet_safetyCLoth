import json
from flask import Blueprint, request, jsonify
from services import admin as s_admin
from utils import utils

admin = Blueprint('admin', __name__)


@admin.route('/register', methods=['POST'])
def register():
    missing_msg = utils.check_missing_params(request, ['userName', 'password'])
    if missing_msg:
        return missing_msg

    data = json.loads(request.data)
    userName = data['userName']
    password = data['password']
    result = s_admin.register(userName, password)
    return result


@admin.route('/login', methods=['POST'])
def login():
    missing_msg = utils.check_missing_params(request, ['userName', 'password'])
    if missing_msg:
        return missing_msg

    data = json.loads(request.data)
    userName = data['userName']
    password = data['password']
    result = s_admin.login(userName, password)
    return result
