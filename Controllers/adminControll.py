from flask import Blueprint,Flask, render_template,request,redirect,url_for, session,flash,jsonify
from flask_restful import Resource,Api
from flask_login import login_user,logout_user, current_user
from sqlalchemy import or_ ,update

from db import db
from Models.admin import Admin
from Models.user import User
from Models.book import Book

adminController = Blueprint('adminController',__name__)


class AdminLogin(Resource):
    def post(self):
        admin = request.form['admin']
        admin_pass = request.form['admin_pass']
        if not admin or not admin_pass:
            print("eksik bilgi")
        else:
            admin = Admin.query.filter_by(admin=admin,admin_pass=admin_pass).first()
            if admin:
                print("giris yapildi")
                return redirect('/admin')
    
        return redirect('/panel')

class UserDelete(Resource):
    def get(self,id):
        user = User.find_user(id)
        User.delete(user)
        print("Kullanici silindi")
        return redirect(url_for("routes.admin_users"))

class MemberSearch(Resource):

    def post(self):
        member_search = request.form['member_search']
        search = "%{}%".format(member_search)
        results = []
        if member_search:
            members = db.session.query(User).filter(User.username.like(search)).all()
            print(members)
            if not members:
                flash("Kayıt bulunamadı")
            for member in members:
                results.append({'username':member.username,
                            'email':member.email})
                print(results)
            return jsonify(results)
            
            
        return redirect(url_for("routes.admin_users"))

class AdminBookSearch(Resource):

    def post(self):
        book_search = request.form.get('admin_book_search')
        search = "%{}%".format(book_search)
        results = []
        if book_search:
            books = db.session.query(Book).filter(or_(Book.title.like(search),Book.author.like(search),Book.barcode.like(search))).all()
            print(books)
            if not books:
                flash("Kayıt bulunamadı")
            for book in books:
                results.append({'title':book.title,
                                'author':book.author,
                                'type':book.type,
                                'barcode':book.barcode,
                                'status':book.status})
                print(results)
            return jsonify(results)
        
        return redirect(url_for("routes.admin"))

