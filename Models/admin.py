
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from Models.db import db

class Admin(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.String(80))
    admin_pass = db.Column(db.String(80))