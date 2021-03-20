import os


from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from server.config import index as cfg

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']=cfg.dbConfig

app.config['SQLALCHEMY_POOL_SIZE']=20

app.config['SQLALCHEMY_POOL_TIMEOUT']=300

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

import server.models.models as models

import server.routes.routes as routes



if __name__ == '__main__':
    app.run(debug=True)
