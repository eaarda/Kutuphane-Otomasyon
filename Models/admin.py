
from flask_login import UserMixin
from db import db

class Admin(UserMixin,db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.String(80))
    admin_pass = db.Column(db.String(80))

    def __init__(self, admin, admin_pass):
        self.admin = admin
        self.admin_pass = admin_pass

    