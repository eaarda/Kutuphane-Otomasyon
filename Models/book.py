
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    author = db.Column(db.String(200))
    type = db.Column(db.String(200))
    barcode = db.Column(db.Integer)
    status = db.Column(db.Boolean, default=True)
