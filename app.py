from flask import Flask, render_template,request,redirect,url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask import flash
from flask_login import LoginManager, UserMixin, login_required, login_user,logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from Models.db import db
from Models.admin import Admin
from Models.user import User
from Models.book import Book
from Models.type import Type

from Controllers.adminControll import adminController
from Controllers.userControll import userController
from Controllers.bookControll import bookController

app = Flask(__name__)
app.register_blueprint(adminController)
app.register_blueprint(userController)
app.register_blueprint(bookController)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Toshiba/Desktop/library/data.db'
app.config['SECRET_KEY'] = 'cokgizli'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def get(id):
    return User.query.get(id)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/panel")
def panel():
    return render_template("adminlogin.html")

@app.route("/admin_book")
def admin_book():
    books = Book.query.all()
    types = Type.query.all()
    return render_template("admin_book.html",books=books,types=types)

@app.route("/admin_users")
def admin_users():
    users = User.query.all()
    return render_template("admin_users.html", users=users)


if __name__ == "__main__":
    app.run(debug = True)

        

        