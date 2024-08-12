import json
from flask import Blueprint, request, jsonify
from services import monitor as s_monitor
from utils import utils

monitor = Blueprint('monitor', __name__)


@monitor.route('/getAll', methods=['GET'])
def getAll():
    result = s_monitor.getAll()
    return result


@monitor.route('/setting', methods=['POST'])
def setting():
    # 查看有没有缺少参数
    missing_msg = utils.check_missing_params(request, ['monitorID', 'isActive'])
    if missing_msg:
        return missing_msg

    data = json.loads(request.data)
    monitorID = data['monitorID']
    isActive = data['isActive']

    result = s_monitor.setting(monitorID, isActive)

    return result


@monitor.route('/add', methods=['POST'])
def add():
    # 查看有没有缺少参数
    missing_msg = utils.check_missing_params(request, ['monitorName', 'source', 'isActive'])
    if missing_msg:
        return missing_msg

    data = json.loads(request.data)
    monitorName = data['monitorName']
    source = data['source']
    isActive = data['isActive']

    result = s_monitor.add(monitorName, source, isActive)
    return result


@monitor.route('/delete', methods=['POST'])
def delete():
    # 查看有没有缺少参数
    missing_msg = utils.check_missing_params(request, ['monitorID'])
    if missing_msg:
        return missing_msg
    data = json.loads(request.data)
    monitorID = data['monitorID']

    result = s_monitor.delete(monitorID)
    return result
