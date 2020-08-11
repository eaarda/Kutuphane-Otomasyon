from flask import Blueprint,Flask, render_template,request,redirect,url_for, session
from flask import flash

from Models.admin import Admin
from Models.user import User
from Models.book import Book
from Models.type import Type

routes = Blueprint('routes',__name__)

@routes.route("/")
def index():
    return render_template("index.html")

@routes.route("/home")
def home():
    return render_template("home.html")

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