from flask import Flask
from flask_login import LoginManager
from flask_restful import Resource,Api

from db import db
from Models.user import User
from Routes.routes import routes

from Controllers import userAuthentication
from Controllers import adminAuthentication
from Controllers import register
from Controllers import bookAdd
from Controllers import books
from Controllers import userControll

app = Flask(__name__)
app.register_blueprint(routes)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Toshiba/Desktop/library/data.db'
app.config['SECRET_KEY'] = 'cokgizli'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
api = Api(app)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
    
@app.before_first_request
def create_tables():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def get(id):
    return User.query.get(id)

api.add_resource(userControll.BorrowBook,'/borrow_book/<string:id>')
api.add_resource(userControll.DeliveryBook,'/delivery_book/<string:id>')
api.add_resource(userControll.Postpone,'/postpone/<string:id>')
api.add_resource(userControll.UserDelete,'/user_delete/<string:id>')
api.add_resource(userControll.BookDelete,'/book_delete/<string:id>')
api.add_resource(userControll.UpdateName,'/update_name')
api.add_resource(userControll.ChangePass,'/change_pass')

api.add_resource(userAuthentication.UserAuthentication, '/user_auth')
api.add_resource(adminAuthentication.AdminAuthentication, '/admin_auth')
api.add_resource(register.Register,'/register')
api.add_resource(bookAdd.BookAdd,'/book_add')
api.add_resource(books.Books,'/books')


if __name__ == "__main__":
    db.init_app(app)
    app.run(debug = True)


        

        