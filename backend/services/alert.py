import datetime
from flask import jsonify
from sqlalchemy.orm import joinedload
from models.alert import Alert
from datetime import datetime
from models.monitor import Monitor
from utils import utils


def get_monthly_alerts():
    now = datetime.now()
    first_day_of_month = now.replace(day=1)
    alerts = Alert.query.options(joinedload(Alert.monitor)).filter(Alert.timestamp >= first_day_of_month).all()

    alert_data = {}
    for alert in alerts:
        monitor_name = alert.monitor.monitorName
        date_str = alert.timestamp.strftime('%Y-%m-%d')
        if monitor_name not in alert_data:
            alert_data[monitor_name] = {'count': 0, 'dates': [], 'counts': {}}
        alert_data[monitor_name]['count'] += 1
        if date_str not in alert_data[monitor_name]['counts']:
            alert_data[monitor_name]['counts'][date_str] = 0
        alert_data[monitor_name]['counts'][date_str] += 1

    for monitor_name in alert_data:
        alert_data[monitor_name]['dates'] = sorted(alert_data[monitor_name]['counts'].keys())

    response_data = []
    total_counts = {'name': 'all', 'count': 0, 'dates': [], 'counts': {}}
    for monitor_name, data in alert_data.items():
        response_data.append({
            'name': monitor_name,
            'count': data['count'],
            'dates': data['dates'],
            'counts': data['counts']
        })
        total_counts['count'] += data['count']
        for date, count in data['counts'].items():
            if date not in total_counts['counts']:
                total_counts['counts'][date] = 0
            total_counts['counts'][date] += count

    total_counts['dates'] = sorted(total_counts['counts'].keys())
    response_data.append(total_counts)

    return jsonify({'code': 0, 'message': 'success', 'data': response_data})



def addOne(iMonitorID, dTimestamp):
    print(iMonitorID,dTimestamp)
    if iMonitorID is None or dTimestamp is None:
        return jsonify({'code': -98, 'message': 'data error', 'data': {}})

    monitorData = Monitor.query.filter_by(monitorID=iMonitorID).first()
    if monitorData is None:
        return jsonify({'code': -1, 'message': 'monitor is not exit', 'data': {}})

    a = Alert(
        monitorID=iMonitorID,
        timestamp=dTimestamp
    )
    if utils.add_model(a) == 0:
        return jsonify({'code': 0, 'message': 'success', 'data': {}})
    else:
        return jsonify({'code': -99, 'message': 'db error', 'data': {}})