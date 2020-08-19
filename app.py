from flask import Flask
from flask_restful import Resource,Api

from db import db
from Controllers.adminControll import adminController,AdminLogin, UserDelete,MemberSearch,AdminBookSearch
from Controllers.userControll import userController, UserRegister, NewUser, BorrowBook,DeliveryBook,Postpone
from Controllers.bookControll import bookController,BookAdd,BookDelete,BookSearch
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
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def get(id):
    return User.query.get(id)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

api.add_resource(NewUser, '/signup', endpoint='user')
api.add_resource(UserRegister, '/login',endpoint='user2')
api.add_resource(UserRegister, '/logout')
api.add_resource(BorrowBook,'/borrow_book/<string:id>')
api.add_resource(DeliveryBook,'/delivery_book/<string:id>')
api.add_resource(Postpone,'/postpone/<string:id>')
api.add_resource(AdminLogin,'/adminlogin')
api.add_resource(UserDelete,'/user_delete/<string:id>')
api.add_resource(MemberSearch,'/member_search')
api.add_resource(AdminBookSearch,'/admin_book_search')
api.add_resource(BookAdd,'/book_add')
api.add_resource(BookDelete,'/book_delete/<string:id>')
api.add_resource(BookSearch,'/book_search')




if __name__ == "__main__":
    db.init_app(app)
    app.run(debug = True)


        

        