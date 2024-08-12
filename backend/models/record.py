from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from db_init import db_init as db


class Record(db.Model):
    __tablename__ = 'record'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    monitorID = db.Column(db.Integer, ForeignKey('monitor.monitorID', ondelete='CASCADE', onupdate='CASCADE'),
                          nullable=False)
    # monitorID = db.Column(db.Integer, nullable=True)

    timestamp = db.Column(db.DateTime, nullable=False)
    # imageURL = db.Column(db.String(255), nullable=True)

    monitor = relationship('Monitor', backref='records')

    def to_dict_withoutID(self):
        return {
            'monitorID': self.monitorID,
            'monitorName': self.monitor.monitorName,  # 添加监控名
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }
