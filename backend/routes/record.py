import json

from flask import Blueprint, request, jsonify
from services import record as s_record
from utils import utils

record = Blueprint('record', __name__)


@record.route('/getAll', methods=['GET'])
def getAll():
    result = s_record.getAll()
    return result


@record.route('/filterByTime', methods=['POST'])
def filterByTime():
    # 查看有没有缺少参数
    missing_msg = utils.check_missing_params(request, ['timestamp'])
    if missing_msg:
        return missing_msg

    data = json.loads(request.data)
    timestamp = data['timestamp']
    result = s_record.filterByTime(timestamp)
    return result


@record.route('/filterByMonitor', methods=['POST'])
def filterByMonitor():
    # 查看有没有缺少参数
    missing_msg = utils.check_missing_params(request, ['monitorID'])
    if missing_msg:
        return missing_msg

    data = json.loads(request.data)
    monitorID = data['monitorID']
    result = s_record.filterByMonitor(monitorID)

    return result


@record.route('/addRecord', methods=['POST'])
def addRecord():
    print(json.loads(request.data))
    missing_msg = utils.check_missing_params(request, ['monitorID', 'timestamp'])
    if missing_msg:
        return missing_msg
    data = json.loads(request.data)
    monitorID = data['monitorID']
    timestamp = data['timestamp']
    print(1)
    result = s_record.addRecord(monitorID, timestamp)
    return result
