
from db import db
from datetime import datetime

class Borrow(db.Model):
    __tablename__ = 'borrow'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    book_id = db.Column(db.Integer,db.ForeignKey('book.id'))
    start_date = db.Column(db.DateTime,default=datetime.utcnow)
    end_date = db.Column(db.DateTime)

    def __init__(self,user_id,book_id,start_date,end_date):
        self.user_id = user_id
        self.book_id = book_id
        self.start_date = start_date
        self.end_date = end_date