from flask import Blueprint,Flask,render_template,request,redirect,url_for, session,flash
from sqlalchemy import or_ ,update

from db import db
from Models.book import Book

bookController = Blueprint('bookController',__name__)

@bookController.route("/book_add",methods=['POST'])
def book_add():
    title =  request.form.get("title")
    author =  request.form.get("author")
    type =  request.form.get('select_type')
    barcode =  request.form.get("barcode")
    existing_book = Book.query.filter_by(barcode=barcode).first()

    if not title or not author or not type or not barcode :
        flash("Tüm alanların doldurulması zorunludur!","wrong")
    elif existing_book:
        flash("Barkod numarası mevcut!","wrong")
    else:
        newBook = Book(title = title, author=author, type=type,barcode=barcode,status=True)
        db.session.add(newBook)
        db.session.commit()
        flash("Kitap kaydedildi","success")
        return redirect(url_for("routes.admin_book"))

    return redirect(url_for("routes.admin_book"))


@bookController.route("/book_delete/<string:id>",methods=['GET','DELETE'])
def book_delete(id):
    book = Book.query.filter_by(id=id).first()
    db.session.delete(book)
    db.session.commit()
    print("kitap silindi")
    return redirect(url_for("routes.admin"))


@bookController.route("/book_search",methods=['POST'])
def book_search():
    book_search = request.form.get('book_search')
    search = "%{}%".format(book_search)
    if book_search:
        books = db.session.query(Book).filter(or_(Book.title.like(search),Book.author.like(search))).all()
        print(books)
        if not books:
            flash("Kayıt bulunamadı")
        return render_template("home.html",books=books)
        
    return redirect(url_for("routes.home"))
