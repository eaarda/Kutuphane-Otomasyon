
from db import db

class Type(db.Model):
    
    __tablename__ = 'type'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80))

    def __init__(self,type):
        self.type = type