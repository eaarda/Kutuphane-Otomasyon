from flask import Flask

from db import db
from Controllers.adminControll import adminController
from Controllers.userControll import userController
from Controllers.bookControll import bookController
from Routes.routes import routes

from Models.user import User
from flask_login import LoginManager, UserMixin, login_user,logout_user, current_user


app = Flask(__name__)
app.register_blueprint(routes)
app.register_blueprint(adminController)
app.register_blueprint(userController)
app.register_blueprint(bookController)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Toshiba/Desktop/library/data.db'
app.config['SECRET_KEY'] = 'cokgizli'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

@app.before_first_request
def create_tables():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def get(id):
    return User.query.get(id)

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug = True)


        

        