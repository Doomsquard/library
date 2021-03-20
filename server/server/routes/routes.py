from flask import request, make_response
from flask_jwt_extended import get_jwt_identity, get_raw_jwt, jwt_refresh_token_required, create_access_token,jwt_required

from server import resourses
from server import app
from server.models import models


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


@app.route('/api/profile',methods=['GET','POST'])
@jwt_required
def get_profile():
    if request.method=='GET':
        try:
            current_user = get_jwt_identity()
            login_user=models.Users.query.filter(models.Users.email==current_user).first()

            books_data=models.Booksprofile.query.filter(models.Booksprofile.login==login_user.login).first()
            login=books_data.login
            birthday = login_user.birthday
            favbooks=books_data.favbooks,
            favgenre=books_data.favgenre
            want_read=books_data.wantread
            readed=books_data.readed
            return make_response({'login':login,
                                  'birthday':birthday,
                                  'favbooks':favbooks,
                                  'favgenre':favgenre,
                                  'want_read':want_read,
                                  'readed':readed},200)
        except:
            return make_response({'message':'Something went wrong'},401)


#-------tokens api--------------------
@app.route('/api/logout/access',methods=['GET','POST'], endpoint='func2')
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
        access_token = create_access_token(identity=current_user)

        return {'access_token': access_token}
