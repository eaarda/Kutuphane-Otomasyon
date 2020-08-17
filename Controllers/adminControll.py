from flask import Blueprint,Flask, render_template,request,redirect,url_for, session,flash
from flask_login import login_user,logout_user, current_user
from sqlalchemy import or_ ,update

from db import db
from Models.admin import Admin
from Models.user import User
from Models.book import Book

adminController = Blueprint('adminController',__name__)

@adminController.route("/adminlogin",methods=['GET','POST'])
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

@adminController.route("/member_search",methods=['POST'])
def member_search():
    member_search = request.form.get('member_search')
    search = "%{}%".format(member_search)

    if member_search:
        members = db.session.query(User).filter(User.username.like(search)).all()
        print(members)
        if not members:
            flash("Kayıt bulunamadı")
        return render_template("admin_users.html",members=members)
        
    return redirect(url_for("routes.admin_users"))

@adminController.route("/admin_book_search",methods=['POST'])
def admin_book_search():
    book_search = request.form.get('admin_book_search')
    search = "%{}%".format(book_search)

    if book_search:
        results = db.session.query(Book).filter(or_(Book.title.like(search),Book.author.like(search),Book.barcode.like(search))).all()
        print(results)
        if not results:
            flash("Kayıt bulunamadı")
        return render_template("admin.html",results = results)
        
    return redirect(url_for("routes.admin"))