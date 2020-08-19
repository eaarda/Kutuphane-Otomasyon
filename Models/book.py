
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


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
          
    def find_book(id):
        return Book.query.filter_by(id=id).first()

    def find_barcode(barcode):
        return Book.query.filter_by(barcode=barcode).first()
    
    def update(self,id):
        return db.session.query(Book).filter_by(id=id).update({"status":False})

    def update2(self,id):
        return db.session.query(Book).filter_by(id=id).update({"status":True})

            

