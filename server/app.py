import os


from flask import Flask, request, make_response, render_template, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, get_raw_jwt, jwt_refresh_token_required, jwt_required, get_jwt_identity, \
    create_access_token

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
    return models.Revokedtokenmodel.is_jti_blacklisted(jti)

import models.models as models
import resourses

@app.route('/getUsers/<email>',methods=['GET'])
def getUser(email):
    users=models.Users.query.filter(models.Users.email==email).first()
    userLogin=models.Login.query.filter(models.Login.email==email).first()
    datereg=userLogin.datereg,
    entries=userLogin.entries
    lastlog=userLogin.lastlog
    login=users.login
    birthday=users.birthday
    return jsonify({"lastlog":lastlog,
                    'datereg':datereg[0],
                    'entries':entries,
                    'email':users.email,
                    'login':login,
                    'birthday':birthday})

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






#-------tokens api--------------------
@app.route('/api/logout/access',methods=['GET','POST'])
@jwt_required
def post():
    jti = get_raw_jwt()['jti']

    try:
        revoked_token = models.Revokedtokenmodel(jti=jti)

        revoked_token.add()

        return make_response({'message': 'Acces token has been revoked'}, 200)

    except:
        return make_response({'message': 'Something went wrong'}, 500)






@app.route('/api/logout/refresh',methods=['GET','POST'])
@jwt_refresh_token_required
def logoutRefresh():
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = models.Revokedtokenmodel(jti=jti)
            revoked_token.add()
            return make_response({'message': 'Acces token has been revoked'}, 200)

        except:
            return make_response({'message': 'Something went wrong'}, 500)



@app.route('/api/token/refresh',methods=['GET','POST'])
@jwt_refresh_token_required
def refreshToken():
        current_user = get_jwt_identity()
        print(current_user)
        access_token = create_access_token(identity=current_user)

        return {'access_token': access_token}


if __name__ == '__main__':
    app.run(debug=True)
