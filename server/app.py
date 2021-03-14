from flask import Flask, jsonify,request,make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


import config.index as cfg
import controllers.signup as sign_up
import controllers.signin as sign_in

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']=cfg.dbConfig

db=SQLAlchemy(app)


#----------------------------CREATE TABLES---------------------------------
class Usertest(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    birthday=db.Column(db.DateTime())

    def __init__(self,username,email,birthday):
        self.username=username
        self.email=email
        self.birthday=birthday

    def __repr__(self):
        return f'<users {self.id}:{self.email}; {self.username}>'


class Login(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(100),unique=True,nullable=False)
    hash=db.Column(db.String(200),nullable=False)
    datereg=db.Column(db.DateTime,nullable=False)
    lastlog=db.Column(db.DateTime,nullable=False)
    entries=db.Column(db.Integer)

    def __init__(self,email,hash,datereg,lastlog,entries):
        self.email=email
        self.hash=u'{}'.format(hash)
        self.datereg=datereg
        self.lastlog=lastlog
        self.entries=entries

    def __repr__(self):
        return f'<login, user email:{self.hash}>'



class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    login = db.Column(db.String(100), unique=True, nullable=False)
    birthday=db.Column(db.DateTime())

    def __init__(self,login,email,birthday):
        self.login=login
        self.email=email
        self.birthday=birthday

    def __repr__(self):
        return f'<users {self.id}:{self.email}; {self.login}>'





#----------------------------------GET----------------------------------
@app.route('/api', methods=['GET'])
def initial():
    print(Users.query.filter(Users.id==1).all())
    return jsonify('hello')



#---------------------------SIGN_IN\SIGN_UP------------------------------
@app.route('/api/auth/signup',methods=['GET','POST'])
def signup():
    if(request.method=='POST'):
        return sign_up.signUp(Users,Login,request,make_response,db)

@app.route('/api/auth/signin',methods=['GET','POST'])
def signin():
    if(request.method=='POST'):
        return sign_in.sign_in(Login,request,make_response,db)




if __name__ == '__main__':
    app.run(debug=True)
