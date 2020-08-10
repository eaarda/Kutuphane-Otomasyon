
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
db = SQLAlchemy(app)

class Admin(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.String(80))
    admin_pass = db.Column(db.String(80))