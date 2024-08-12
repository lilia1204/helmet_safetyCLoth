from db_init import db_init as db


class Admin(db.Model):
    __tablename__ = 'admin'
    userName = db.Column(db.String(255), primary_key=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'userName': self.userName,
            'password': self.password,
        }
