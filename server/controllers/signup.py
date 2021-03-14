import hashPas
import datetime


def signUp(Users,Login,request,make_response,db):

    #res=db.session.query(Users,Login).join(Login,Users.email==Login.email).all()

    hashPassword=hashPas.hash(request.json["password"]).decode('utf-8')
    dateReg=datetime.datetime.now()
    print(hashPassword)
    login=Login(email=request.json['email'],hash=hashPassword,datereg=dateReg,lastlog=dateReg,entries=1)
    user=Users(login=request.json['login'],email=request.json['email'],birthday=request.json['birthday'])
    try:
        if len(Users.query.filter(Users.email==request.json['email']).all())==True:
            return make_response({"message":'Пользователь с таким Email уже существует'}, 400)

        elif len(Users.query.filter(Users.login==request.json['login']).all())==True:
            return make_response({"message":'Пользователь с таким login уже существует'},400)
        else:
            db.session.add(login)
            db.session.add(user)
            db.session.commit()
            return make_response({"message":'Пользователь зарегистрирован'}, 200)
    except:
        return make_response({"message":'Что-то пошло не так'},400)
