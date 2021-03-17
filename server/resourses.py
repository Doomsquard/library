from flask import request, jsonify, make_response
from flask_jwt_extended import (
jwt_required,get_raw_jwt,jwt_refresh_token_required,get_jwt_identity,create_access_token
)

from app import app, db

import controllers.signup as sign_up
import controllers.signin as sign_in
import models.models as models


def initial():
    return ('hello')



def user_by_id(login):
    if (request.method == 'GET'):
        currentUser = models.Booksprofile.query.filter(models.Booksprofile.login == login).first()
        if currentUser:
            login = currentUser.login
            favbooks = currentUser.favbooks
            favgenre = currentUser.favgenre
            wantread = currentUser.wantread
            readed = currentUser.readed

            return make_response(jsonify({
                "login": login,
                "favboooks": favbooks,
                "favgenre": favgenre,
                "wantread": wantread,
                "readed": readed
            }), 200)
        else:
            return make_response('Пользователь не найден', 400)


# ---------------------------SIGN_IN\SIGN_UP------------------------------

def signup():
    if (request.method == 'POST'):
        return sign_up.signUp(models.Users, models.Login, models.Booksprofile, request, make_response, db)



def signin():
    if (request.method == 'POST'):
        return sign_in.sign_in(models.Login, request, make_response, db)


def log_acces():
    if request.method == 'POST':
        @jwt_required
        def post():
            jti = get_raw_jwt()['jti']

            try:
                revoked_token = models.RevokedTokenModel(jti=jti)

                revoked_token.add()

                return make_response({'message': 'Acces token has been revoked'}, 200)

            except:
                return make_response({'message': 'Something went wrong'}, 500)
        post()

def log_refresh():
    @jwt_refresh_token_required
    def post():
        jti = get_raw_jwt()['jti']

        try:
            revoked_token = models.RevokedTokenModel(jti=jti)

            revoked_token.add()

            return make_response({'message': 'Acces token has been revoked'}, 200)

        except:
            return make_response({'message': 'Something went wrong'}, 500)
    post()

def token_refresh():
    @jwt_refresh_token_required
    def post():
        current_user = get_jwt_identity()
        print(current_user)
        access_token = create_access_token(identity=current_user)

        return {'access_token': access_token}
    post()