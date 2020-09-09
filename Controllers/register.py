from flask import Flask, request,redirect,flash
from flask_restful import Resource,Api
from flask_login import login_user

from db import db
from Models.user import User

class Register(Resource):
    def post(self):
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        existing_user = User.query.filter_by(email=email).first()
        
        if not username or not email or not password :
            flash("Tüm alanları doldurun!","signup")
        elif existing_user:
            flash("Geçersiz email adresi!","signup")
        else:
            user = User(username=username, email=email, password=password)
            user.save()
            login_user(user)
            return redirect('/home')
        return redirect('/')