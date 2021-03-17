import hashPas
import datetime

from flask_jwt_extended import (
create_access_token,create_refresh_token
)


def signUp(Users,Login,Booksprofile,request,make_response,db):

    currentLogin=request.json['login']
    currentEmail=request.json['email']



    hashPassword=hashPas.hash(request.json["password"]).decode('utf-8')
    dateReg=datetime.datetime.now()

    print(Booksprofile.query.all(),Login)
    login=Login(email=currentEmail,hash=hashPassword,datereg=dateReg,lastlog=dateReg,entries=1)
    user=Users(login=currentLogin,email=currentEmail,birthday=request.json['birthday'])
    booksUser=Booksprofile(login=currentLogin,favbooks=[''],favgenre=[''],wantread=0,readed=0)
    try:
        if len(Users.query.filter(Users.email==request.json['email']).all())==True:
            return make_response({"message":'Пользователь с таким Email уже существует'}, 404)

        elif len(Users.query.filter(Users.login==request.json['login']).all())==True:
            return make_response({"message":'Пользователь с таким login уже существует'},404)
        else:
            db.session.add(login)
            db.session.add(user)
            db.session.add(booksUser)
            db.session.commit()
            access_token=create_access_token(identity=currentEmail)
            refresh_token=create_refresh_token(identity=currentEmail)
            return make_response({"message":f'Пользователь {currentEmail} зарегистрирован',
                                  "access_token":access_token,
                                  "refresh_token":refresh_token}, 200)
    except:
        return make_response({"message":'Что-то пошло не так'},500)
