from flask import Flask,request,redirect,url_for,flash
from flask_restful import Resource,Api
from flask_login import current_user
from sqlalchemy import or_ ,update

from datetime import datetime  
from datetime import timedelta  

from db import db
from Models.user import User
from Models.book import Book
from Models.borrow import Borrow

class BorrowBook(Resource): #post
    def get(self,id):
        b = Book.update(self,id)
        limit = db.session.query(Borrow,Book).filter(Borrow.user_id == current_user.id).filter(Borrow.book_id== Book.id).count()
        print(limit)
        if limit > 4:
            flash("Daha fazla kitap alamazsınız")
            return redirect(url_for("routes.home"))
        else:
            db.session.query(Borrow,Book).filter(Borrow.user_id == current_user.id).filter(Borrow.book_id== Book.id)
            newBorrow = Borrow(user_id = current_user.id, book_id = id, start_date = datetime.now(), end_date = datetime.now() + timedelta(days=5))
            Borrow.save(newBorrow)
        return redirect(url_for("routes.user_book"))


class DeliveryBook(Resource): #delete
    def get(self,id):
        d = Book.update2(self,id)
        delivery = Borrow.query.filter_by(book_id=id).first()
        Borrow.delete(delivery)
        return redirect (url_for("routes.user_book"))


class Postpone(Resource): #put
    def get(self,id):
        p = db.session.query(Borrow).filter_by(id=id).update({"end_date": datetime.now() + timedelta(days=5)})
        db.session.commit()
        print("tarih değişti")
        return redirect(url_for("routes.user_book"))


class UpdateName(Resource):  #put
    def post(self):
        new = request.form.get('username')
        if not new:
            flash("Yeni bir kullanıcı adı girin","name")
        else:
            x = db.session.query(User).filter_by(id = current_user.id).update({"username": new})
            db.session.commit()
            flash("Kullanıcı adı değiştirildi","name2")
            print("kullanici adi degisti")

        return redirect('/profile')

class ChangePass(Resource):  #put
    def post(self):
        new = request.form.get('password')
        print(new)
        if not new:
            flash("Yeni bir şifre girin","pass")
        else:
            x = db.session.query(User).filter_by(id=current_user.id).update({"password": new})
            db.session.commit()
            print("sifre degistirildi")
            flash("Şifre değiştirildi","pass2")
        return redirect('/profile')


class UserDelete(Resource):  #delete 
    def get(self,id):
        user = User.find_user(id)
        User.delete(user)
        print("Kullanici silindi")
        return redirect(url_for("routes.admin_users"))


class BookDelete(Resource):  #delete
    def get(self,id):
        book = Book.find_book(id)
        Book.delete(book)
        print("kitap silindi")
        return redirect(url_for("routes.admin"))

