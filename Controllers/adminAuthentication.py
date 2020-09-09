from flask import Flask, request,redirect,flash
from flask_restful import Resource,Api
from flask_login import logout_user

from db import db
from Models.admin import Admin

class AdminAuthentication(Resource):

    def post(self):
        admin = request.form['admin']
        admin_pass = request.form['admin_pass']
        if not admin or not admin_pass:
            print("eksik bilgi")
        else:
            admin = Admin.query.filter_by(admin=admin,admin_pass=admin_pass).first()
            if admin:
                return redirect('/admin')
    
        return redirect('/panel')
    
    def get(self):
        logout_user()
        return redirect('/')

