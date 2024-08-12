from flask import jsonify
from models.monitor import Monitor
from models.alert import Alert
from models.record import Record
from utils import utils


def getAll():
    monitorData = Monitor.query.all()
    monitorDicts = [m.to_dict() for m in monitorData]
    print(monitorDicts)
    return jsonify({'code': 0, 'message': 'success', 'data': monitorDicts})


def setting(iMonitorID, bIsActive):
    if iMonitorID is None or bIsActive is None:
        return jsonify({'code': -98, 'message': 'data error', 'data': {}})
    m = Monitor.query.filter_by(monitorID=iMonitorID).first()
    if m is None:
        return jsonify({'code': -1, 'message': 'monitorID not exit', 'data': {}})
    if utils.update_model(m, {'isActive': bIsActive}) != 0:
        return jsonify({'code': -99, 'message': 'db error', 'data': {}})
    return jsonify({'code': 0, 'message': 'success', 'data': {}})


def add(sMonitorName, sSource, bIsActive):
    if sMonitorName is None or sSource is None or bIsActive is None:
        return jsonify({'code': -98, 'message': 'data error', 'data': {}})
    m = Monitor(
        monitorName=sMonitorName,
        isActive=1,
        source=sSource
    )
    if utils.add_model(m) == 0:
        return jsonify({'code': 0, 'message': 'success', 'data': {}})
    else:
        return jsonify({'code': -99, 'message': 'db error', 'data': {}})


def delete(iMonitorID):
    print(iMonitorID)
    if iMonitorID is None:
        return jsonify({'code': -98, 'message': 'data error', 'data': {}})


    a=Alert.query.filter_by(monitorID=iMonitorID).all()
    if a:
        for instance in a:
            utils.delete_model(instance)


    r = Record.query.filter_by(monitorID=iMonitorID).all()
    if r:
        for instance in r:
            utils.delete_model(instance)

    m = Monitor.query.filter_by(monitorID=iMonitorID).first()

    msg = utils.delete_model(m)
    if msg == 0:
        return jsonify({'code': 0, 'message': 'success', 'data': {}})
    elif msg == -1:
        return jsonify({'code': -99, 'message': 'db error', 'data': {}})
    elif msg == -2:
        return jsonify({'code': -1, 'message': 'monitor not exit', 'data': {}})
