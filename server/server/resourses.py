from flask import request, jsonify, make_response


from server import db

from server.controllers import signup as sign_up
from server.controllers import signin as sign_in
from server.models import models


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




