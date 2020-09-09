from flask import Flask, request,redirect,flash
from flask_restful import Resource,Api
from flask_login import login_user,logout_user

from db import db
from Models.user import User

class UserAuthentication(Resource):
    
    def post(self):
        email = request.form['email']
        password = request.form['password']
        wrong = User.query.filter_by(email=email,password=password).first()
        if not email or not password:
            flash("Geçersiz email veya şifre","login")
        elif not wrong:
            flash("Geçersiz email veya şifre","login")
        else:
            user = User.query.filter_by(email=email,password=password).first()
            login_user(user)
            return redirect('/home')
        return redirect('/')

    def get(self):
        logout_user()
        return redirect('/')