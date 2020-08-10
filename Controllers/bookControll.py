from flask import Blueprint,Flask, render_template,request,redirect,url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask import flash

from Models.db import db
from Models.book import Book

bookController = Blueprint('bookController',__name__)

@bookController.route("/book_add",methods=['POST'])
def book_add():
    title =  request.form.get("title")
    author =  request.form.get("author")
    type =  request.form.get('select_type')
    print(type)
    barcode =  request.form.get("barcode")

    if not title or not author or not type or not barcode :
        print("eksik bilgi")

    existing_book = Book.query.filter_by(barcode=barcode).first()
    if existing_book:
        print("book already exists")
    else:
        newBook = Book(title = title, author=author, type=type,barcode=barcode,status=True)
        db.session.add(newBook)
        db.session.commit()
        print("kitap kaydedildi")
        return redirect(url_for("routes.admin_book"))

    return redirect(url_for("routes.admin_book"))


@bookController.route("/book_delete/<string:id>")
def book_delete(id):
    book = Book.query.filter_by(id=id).first()
    db.session.delete(book)
    db.session.commit()
    print("kitap silindi")
    return redirect(url_for("routes.admin_book"))