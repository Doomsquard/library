import os


from flask import Flask,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

import config.index as cfg

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']=cfg.dbConfig

app.config['SECRET_KEY']=os.getenv('SECRET_KEY','my_precious')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.config['JWT_SECRET_KEY'] = 'Dude!WhyShouldYouEncryptIt'

app.config['JWT_BLACKLIST_ENABLED'] = True

app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']


db=SQLAlchemy(app)
jwt=JWTManager(app)

@app.before_first_request
def create_tables():
    db.create_all()


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti=decrypted_token['jti']

    return models.RevokenTokenModel.is_jti_blacklisted(jti)

import models.models as models
import resourses


@app.route('/api', methods=['GET'])
def initial():
    return resourses.initial()

@app.route('/api/user/<login>', methods=['GET', 'POST'])
def user_by_id(login):
    return resourses.user_by_id(login)

@app.route('/api/auth/signup', methods=['GET', 'POST'])
def signup():
    return resourses.signup()

@app.route('/api/auth/signin', methods=['GET', 'POST'])
def signin():
    return resourses.signin()


@app.route('/api/logout/access',methods=['GET','POST'])
def log_access():
    resourses.log_acces()

@app.route('/api/logout/refresh',methods=['GET','POST'])
def log_refresh():
    resourses.log_refresh()

@app.route('/api/token/refresh',methods=['GET','POST'])
def token_refresh():
    resourses.token_refresh()

if __name__ == '__main__':
    app.run(debug=True)
