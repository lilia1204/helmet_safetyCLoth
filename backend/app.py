from db_init import app
from routes.record import record
from routes.admin import admin
from routes.monitor import monitor
from routes.alert import alert


# 路由设置
# 健康检查路由
@app.route('/')
def ping():
    return 'ok'


app.register_blueprint(record, url_prefix="/record")
app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(monitor, url_prefix='/monitor')
app.register_blueprint(alert, url_prefix='/alert')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
