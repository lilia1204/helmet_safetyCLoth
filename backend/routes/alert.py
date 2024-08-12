import json
from flask import Blueprint, request, jsonify
from services import alert as s_alert
from utils import utils

alert = Blueprint('alert', __name__)


@alert.route('/monthly', methods=['GET'])
def get_monthly_alerts_route():
    return s_alert.get_monthly_alerts()


@alert.route('/addOne', methods=['POST'])
def addOne():
    missing_msg = utils.check_missing_params(request, ['monitorID', 'timestamp'])
    if missing_msg:
        return missing_msg

    data = json.loads(request.data)
    monitorID = data['monitorID']
    timestamp = data['timestamp']

    result = s_alert.addOne(monitorID, timestamp)
    return result