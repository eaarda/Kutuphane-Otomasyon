
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from Models.db import db


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))