
from db import db

class Book(db.Model):
    __tablename__ = 'book'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    author = db.Column(db.String(200))
    type = db.Column(db.String(200),db.ForeignKey('type.id'))
    barcode = db.Column(db.Integer)
    status = db.Column(db.Boolean, default=True)

    def __init__(self, title, author, type, barcode, status):
        self.title = title
        self.author = author
        self.type = type
        self.barcode = barcode
        self.status = status
