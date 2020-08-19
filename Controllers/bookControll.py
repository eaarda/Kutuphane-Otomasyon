from flask import Blueprint,Flask,render_template,request,redirect,url_for, session,flash
from flask_restful import Resource,Api
from sqlalchemy import or_ ,update

from db import db
from Models.book import Book

bookController = Blueprint('bookController',__name__)


class BookAdd(Resource):
    def post(self):
        title =  request.form.get("title")
        author =  request.form.get("author")
        type =  request.form.get('select_type')
        barcode =  request.form.get("barcode")
        existing_book = Book.find_barcode(barcode)

        if not title or not author or not type or not barcode :
            flash("Tüm alanların doldurulması zorunludur!","wrong")
        elif existing_book:
            flash("Barkod numarası mevcut!","wrong")
        else:
            newBook = Book(title = title, author=author, type=type,barcode=barcode,status=True)
            Book.save(newBook)
            flash("Kitap kaydedildi","success")
            return redirect(url_for("routes.admin_book"))

        return redirect(url_for("routes.admin_book"))

class BookDelete(Resource):
    def get(self,id):
        book = Book.find_book(id)
        Book.delete(book)
        print("kitap silindi")
        return redirect(url_for("routes.admin"))

class BookSearch(Resource):
    def post(self):
        book_search = request.form.get('book_search')
        search = "%{}%".format(book_search)
        if book_search:
          books = db.session.query(Book).filter(or_(Book.title.like(search),Book.author.like(search))).all()
          print(books)
          if not books:
              flash("Kayıt bulunamadı")
          return render_template("home.html",books=books)
        
        return redirect(url_for("routes.home"))