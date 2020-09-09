from flask import Flask,redirect,url_for
from flask_restful import Resource,Api

from db import db
from Models.book import Book

class Books(Resource):
    def get(self):
        books = Book.query.all()
        print(books)
        results=[]
        for book in books:
            results.append({'title':book.title,
                            'author':book.author,
                            'type':book.type,
                            'barcode':book.barcode,
                            'status':book.status,
                            'imgname':book.imgname,
                            'mimetype':book.mimetype})
            print(results)
        return results,200

