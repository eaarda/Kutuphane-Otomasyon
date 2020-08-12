from flask import Blueprint,Flask, render_template,request,redirect,url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask import flash
from flask_login import LoginManager, UserMixin, login_required, login_user,logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_ ,update
from datetime import datetime

from Models.db import db
from Models.user import User
from Models.book import Book
from Models.borrow import Borrow

userController = Blueprint('userController',__name__)

@userController.route("/login", methods=['GET','POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if not email or not password:
        print("eksik bilgi")
    else:
        user = User.query.filter_by(email=email,password=password).first()
        login_user(user)
        print("giris yapildi")
        return redirect('/home')
        
    return render_template("index.html")


@userController.route("/signup" , methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    if not username or not email or not password :
        print("eksik bilgi")
    
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        print("already exists")
        return render_template("index.html")
    else:
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect('/home')
        print("kayit olundu")

    return render_template("index.html")


@userController.route("/logout",methods=['GET'])
def logout():
    logout_user()
    return redirect('/')

@userController.route("/borrow_book/<string:id>")
def borrow_book(id):
    borrow = db.session.query(Book).filter_by(id=id).update({"status":False})
    print(borrow)

    newBorrow = Borrow(user_id = current_user.id, book_id = id)
    #start_date=datetime.strptime(start_date, "%Y-%m-%d").date()
    db.session.add(newBorrow)
    db.session.commit()
    print(newBorrow)
    print("odunc alindi")

    return redirect(url_for("routes.user_book"))

