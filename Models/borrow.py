
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Models.db import db
from datetime import datetime

class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    book_id = db.Column(db.Integer)
    start_date = db.Column(db.DateTime,default=datetime.utcnow)
    end_date = db.Column(db.DateTime)