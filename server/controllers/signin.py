import datetime
import hashPas

from flask_jwt_extended import (
create_access_token,create_refresh_token
)

def sign_in(Login,request,make_response,db):
    email=request.json['email']
    password=request.json['password']
    user=Login.query.filter(Login.email==email).first()
    if not user:
        return make_response({'message': 'Email or password incorrect'}, 400)

    hash=user.hash
    truePas=hashPas.check(password,hash)
    if truePas:
        user=Login.query.filter(Login.email==email)
        entries=user.first().entries
        entries=entries+1
        user.update({'lastlog':datetime.datetime.now(),"entries":entries})
        db.session.commit()
        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)
        return make_response({"message": f'Пользователь {email} вошел в систему',
                              "access_token": access_token,
                              "refresh_token": refresh_token}, 200)
    else:
        return make_response({'message':'Email or password incorrect'},400)