from flask import Blueprint,Flask, render_template,request,redirect,url_for, session,flash
from flask_restful import Resource,Api
from flask_login import  UserMixin, login_user,logout_user, current_user
from sqlalchemy import or_ ,update

from datetime import datetime  
from datetime import timedelta  

from db import db
from Models.user import User
from Models.book import Book
from Models.borrow import Borrow

userController = Blueprint('userController',__name__)

class NewUser(Resource):

    def post(self):
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        existing_user = User.query.filter_by(email=email).first()
        
        if not username or not email or not password :
            flash("Tüm alanları doldurun!","signup")
        elif existing_user:
            flash("Geçersiz email adresi!","signup")
        else:
            user = User(username=username, email=email, password=password)
            user.save()
            login_user(user)
            return redirect('/home')
        return redirect('/')

class UserRegister(Resource):
    
    def post(self):
        email = request.form['email']
        password = request.form['password']
        wrong = User.query.filter_by(email=email,password=password).first()
        if not email or not password:
            flash("Geçersiz email veya şifre","login")
        elif not wrong:
            flash("Geçersiz email veya şifre","login")
        else:
            user = User.query.filter_by(email=email,password=password).first()
            login_user(user)
            return redirect('/home')

        return redirect('/')

    def get(self):
        logout_user()
        print("cikiss")
        return redirect('/')

class BorrowBook(Resource):

    def get(self,id):
        b = Book.update(self,id)
        newBorrow = Borrow(user_id = current_user.id, book_id = id, start_date = datetime.now(), end_date = datetime.now() + timedelta(days=5))
        Borrow.save(newBorrow)
        return redirect(url_for("routes.user_book"))
    
class DeliveryBook(Resource):

    def get(self,id):
        d = Book.update2(self,id)
        delivery = Borrow.query.filter_by(book_id=id).first()
        Borrow.delete(delivery)
        return redirect (url_for("routes.user_book"))

class Postpone(Resource):

    def get(self,id):
        p = db.session.query(Borrow).filter_by(id=id).update({"end_date": datetime.now() + timedelta(days=5)})
        db.session.commit()
        print("tarih değişti")
        return redirect(url_for("routes.user_book"))

