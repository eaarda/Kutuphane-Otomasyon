from flask import Blueprint,Flask, render_template,request,redirect,url_for, session,flash
from flask_login import current_user
import datetime

from db import db
from Models.admin import Admin
from Models.user import User
from Models.book import Book
from Models.type import Type
from Models.borrow import Borrow

from Controllers.bookControll import BookSearch

routes = Blueprint('routes',__name__)

@routes.route("/")
def index():
    return render_template("index.html")

@routes.route("/home")
def home():
    return render_template("home.html")

@routes.route("/admin")
def admin():
    books = Book.query.all()
    return render_template("admin.html",books=books)

@routes.route("/panel")
def panel():
    return render_template("adminlogin.html")

@routes.route("/admin_book")
def admin_book():
    types = Type.query.all()
    return render_template("admin_book.html",types=types)

@routes.route("/admin_users")
def admin_users():
    users = User.query.all()
    return render_template("admin_users.html", users=users)

@routes.route("/user_book")
def user_book():

    orders = db.session.query(Borrow,Book).filter(Borrow.user_id == current_user.id).filter(Borrow.book_id== Book.id).all()
    print(orders)

    def convertdate(rdate):
        cdate=datetime.datetime.strptime(str(rdate).split(" ")[0], "%Y-%m-%d").date()
        return cdate

    return render_template("user_book.html",orders=orders,convertdate=convertdate)