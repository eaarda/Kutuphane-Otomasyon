from flask import Blueprint,Flask, render_template,request,redirect,url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask import flash
from flask_login import LoginManager, UserMixin, login_required, login_user,logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from Models.db import db
from Models.admin import Admin
from Models.user import User

adminController = Blueprint('adminController',__name__)

@adminController.route("/adminlogin",methods=['POST'])
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
    
    return render_template("/adminlogin.html")

@adminController.route("/logout",methods=['GET'])
def logout():
    logout_user()
    return redirect('/')


@adminController.route("/user_delete/<string:id>",methods=['GET','DELETE'])
def user_delete(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    print("Kullanici silindi")
    return redirect(url_for("routes.admin_users"))