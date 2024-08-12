from db_init import db_init as db


class Monitor(db.Model):
    __tablename__ = 'monitor'
    monitorID = db.Column(db.Integer, primary_key=True, nullable=True)
    monitorName = db.Column(db.String(255), nullable=False)
    isActive = db.Column(db.Boolean, nullable=False)
    source = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'monitorID': self.monitorID,
            'monitorName': self.monitorName,
            'isActive': self.isActive,
            'source': self.source,
        }
