from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Toshiba/Desktop/library/data.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add",methods = ["POST"])
def addUser():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    newUser = User(username = username, email = email, password = password)

    db.session.add(newUser)
    db.session.commit()
    return redirect(url_for("index"))


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))


if __name__ == "__main__":
    app.run(debug = True)

        

        