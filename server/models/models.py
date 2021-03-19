from app import db

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

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_login(cls,username):
        return cls.query.filter(cls.username==username).first()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'login':x.login,
                'password':x.password
            }
        return {'users':[to_json(user) for user in cls.query.all()]}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted=db.session.query(cls).delete()
            db.session.commit()

            return {'message':f'{num_rows_deleted} row(s) deleted'}

        except:
            return {'message':'something went wrong'}


class Revokedtokenmodel(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    jti=db.Column(db.String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls,jti):
        query=cls.query.filter(Revokedtokenmodel.jti==jti).first()
        return bool(query)


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

class Booksprofile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), unique=True, nullable=False)
    favbooks=db.Column(db.ARRAY(db.String()))
    favgenre=db.Column(db.ARRAY(db.String()))
    wantread=db.Column(db.Integer)
    readed=db.Column(db.Integer)

    def __init__(self,login,favbooks,favgenre,wantread,readed):
        self.login=login,
        self.favbooks=favbooks
        self.favgenre=favgenre,
        self.wantread=wantread,
        self.readed=readed

    def __repr__(self):
        return f'<Booksprofile {self.login}>'



