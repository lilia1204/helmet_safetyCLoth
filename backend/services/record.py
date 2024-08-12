import re
import time

from flask import jsonify

from db_init import db_init as db
from models.record import Record
from utils import utils


def getAll():
    recordData = Record.query.all()
    rDicts = [r.to_dict_withoutID() for r in recordData]
    return jsonify({'code': 0, 'message': 'success', 'data': rDicts})


def filterByMonitor(iMonitorID):
    if iMonitorID is None:
        return jsonify({'code': -98, 'message': 'data error', 'data': {}})

    recordData = Record.query.filter_by(monitorID=iMonitorID).all()
    rDicts = [r.to_dict_withoutID() for r in recordData]
    return jsonify({'code': 0, 'message': 'success', 'data': rDicts})


def filterByTime(dTimestamp):
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    if not re.match(date_pattern, dTimestamp):
        return jsonify({'code': -98, 'message': 'data error', 'data': {}})

    recordData = Record.query.filter(db.func.date(Record.timestamp) == dTimestamp).all()
    rDicts = [r.to_dict_withoutID() for r in recordData]
    return jsonify({'code': 0, 'message': 'success', 'data': rDicts})


def addRecord(iMonitorID, dTimestamp):
    print(dTimestamp)
    if iMonitorID is None or dTimestamp is None:
        return jsonify({'code': -98, 'message': 'data error', 'data': {}})

    r = Record(
        monitorID=iMonitorID,
        timestamp=dTimestamp
    )
    if utils.add_model(r) == 0:
        return jsonify({'code': 0, 'message': 'success', 'data': {}})
    else:
        return jsonify({'code': -99, 'message': 'db error', 'data': {}})
