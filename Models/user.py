
from flask_login import UserMixin
from db import db


class User(UserMixin,db.Model):
    
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password


    def find_user(id):
        return User.query.filter_by(id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    
