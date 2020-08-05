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


@app.route("/login", methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(email=email).first()
    login_user(user)
    return render_template("home.html")

@app.route("/signup" , methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    user = User.query.filter_by(email=email).first()
    login_user(user)
    return render_template("home.html")

@app.route("/logout",methods=['GET'])
def logout():
    logout_user()
    return redirect('/')










class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

if __name__ == "__main__":
    app.run(debug = True)

        

        