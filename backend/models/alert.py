from db_init import db_init as db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Alert(db.Model):
    __tablename__ = 'alert'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    monitorID = db.Column(db.Integer, ForeignKey('monitor.monitorID', ondelete='CASCADE', onupdate='CASCADE'),
                          nullable=False)
    # monitorID = db.Column(db.Integer,
    #                       nullable=True)
    timestamp = db.Column(db.DateTime, nullable=False)

    monitor = relationship('Monitor', backref='alerts')

    def to_dict(self):
        return {
            'monitorID': self.monitorID,
            'timestamp': self.timestamp,
        }
