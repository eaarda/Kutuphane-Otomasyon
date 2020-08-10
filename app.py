from flask import Flask, render_template,request,redirect,url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask import flash
from flask_login import LoginManager, UserMixin, login_required, login_user,logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Toshiba/Desktop/library/data.db'
app.config['SECRET_KEY'] = 'cokgizli'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

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

@app.route("/adminlogin",methods=['POST'])
def adminlogin():
    admin = request.form['admin']
    admin_pass = request.form['admin_pass']
    if not admin or not admin_pass:
        print("eksik bilgi")
    else:
        admin = Admin.query.filter_by(admin=admin,admin_pass=admin_pass).first()
        if admin:
            print("giris yapildi")
            return redirect('/admin')
    
    return render_template("adminlogin.html")

@app.route("/login", methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if not email or not password:
        print("eksik bilgi")
    else:
        user = User.query.filter_by(email=email,password=password).first()
        login_user(user)
        print("giris yapildi")
        return render_template("home.html")
    return render_template("index.html")

@app.route("/signup" , methods=['POST'])
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
        return render_template("home.html")
        print("kayit olundu")

    return render_template("index.html")

@app.route("/logout",methods=['GET'])
def logout():
    logout_user()
    return redirect('/')

@app.route("/book_add",methods=['POST'])
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
        return redirect(url_for("admin_book"))

    return redirect(url_for("admin_book"))

@app.route("/book_delete/<string:id>")
def book_delete(id):
    book = Book.query.filter_by(id=id).first()
    db.session.delete(book)
    db.session.commit()
    print("kitap silindi")
    return redirect(url_for("admin_book"))

@app.route("/user_delete/<string:id>")
def user_delete(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    print("Kullanici silindi")
    return redirect(url_for("admin_users"))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    author = db.Column(db.String(200))
    type = db.Column(db.String(200))
    barcode = db.Column(db.Integer)
    status = db.Column(db.Boolean, default=True)
class Admin(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.String(80))
    admin_pass = db.Column(db.String(80))
class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80))
    



if __name__ == "__main__":
    app.run(debug = True)

        

        