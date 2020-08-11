from flask import Blueprint,Flask, render_template,request,redirect,url_for, session
from flask import flash,session


from Models.db import db
from Models.admin import Admin
from Models.user import User
from Models.book import Book
from Models.type import Type

from Controllers.bookControll import book_search

routes = Blueprint('routes',__name__)

@routes.route("/")
def index():
    return render_template("index.html")

@routes.route("/home")
def home():
    types = Type.query.all()
    results = book_search()
    return render_template("home.html",types=types,results=results)

@routes.route("/admin")
def admin():
    return render_template("admin.html")

@routes.route("/panel")
def panel():
    return render_template("adminlogin.html")

@routes.route("/admin_book")
def admin_book():
    books = Book.query.all()
    types = Type.query.all()
    return render_template("admin_book.html",books=books,types=types)

@routes.route("/admin_users")
def admin_users():
    users = User.query.all()
    return render_template("admin_users.html", users=users)