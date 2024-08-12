from flask_sqlalchemy import SQLAlchemy
from config import config
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.json.ensure_ascii = False


app.config['SQLALCHEMY_DATABASE_URI'] = config.url
# 数据库初始化对象
db_init = SQLAlchemy(app)
