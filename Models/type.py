
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Models.db import db

class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80))