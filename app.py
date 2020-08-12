from flask import Flask, render_template,request,redirect,url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask import flash
from flask_login import LoginManager, UserMixin, login_required, login_user,logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from Models.user import User

from Controllers.adminControll import adminController
from Controllers.userControll import userController
from Controllers.bookControll import bookController
from Routes.routes import routes

app = Flask(__name__)
app.register_blueprint(routes)
app.register_blueprint(adminController)
app.register_blueprint(userController)
app.register_blueprint(bookController)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Toshiba/Desktop/library/data.db'
app.config['SECRET_KEY'] = 'cokgizli'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def get(id):
    return User.query.get(id)


if __name__ == "__main__":
    app.run(debug = True)

        

        