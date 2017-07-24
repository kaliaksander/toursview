from flask import Flask, render_template, redirect, url_for ,request, session, flash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import input_required,email,length
from flask_bootstrap import Bootstrap
#import sqlite3

app = Flask(__name__)
Bootstrap(app)

class LoginForm(FlaskForm):
    username = StringField('username',validators=[input_required(),length(min=4,max=15)])
    password = PasswordField('password',validators=[input_required(),length(min=8,max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email',validators=[input_required(),email(message='invalid email'),length(max=50)])
    username = StringField('username', validators=[input_required(), length(min=4, max=15)])
    password = PasswordField('password', validators=[input_required(), length(min=8, max=80)])
# config
app.config.from_object('config.DevelopmentConfig')

# create the sqlalchemy object
db = SQLAlchemy(app)

from models import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1>'+form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html',form=form)

@app.route('/signup',methods=['GET','POST'])
def  signup():
    form=RegisterForm()
    if form.validate_on_submit():
        return '<h1>'+form.username.data + ' ' + form.email.data + ' ' + form.password.data +  '</h1>'
    return render_template('signup.html',form=form)

@app.route('/dashboard')
def welcome():
    return render_template('dashboard.html')

if __name__=='__main__':
    app.run(debug=True)