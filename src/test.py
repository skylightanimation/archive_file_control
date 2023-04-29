
import os
from flask import Flask,  request, url_for, redirect, flash #, render_template, session
from flask_sqlalchemy import SQLAlchemy
# from flask_hashing import Hashing
from sqlalchemy.sql import func
from systems import database, security


class Config:
    _db = {}
    _db['uname'] = 'root'
    _db['pswd'] = ''
    _db['host'] = 'localhost'
    _db['port'] = '3306'
    _db['db'] = 'raitostproject_ff_db'

    print(_db)


print(Config._db)



class Database():
    # print(config._configuration)
    __access = Config._db
    _connection = 'mysql://'+__access["uname"]+':'+__access["pswd"]+'@'+__access["host"]+':'+__access["port"]+'/'+__access["db"]


print(Database._connection)


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = Database._connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.secret_key = security.BlackJack._secret
db = SQLAlchemy(app)
