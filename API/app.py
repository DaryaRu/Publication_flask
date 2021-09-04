from flask import Flask
from flask_restful import Api
from resources.healthcheck import Healthcheck
from db import db
from resources.rubric import Rubric, RubricList
from resources.like import Like
from flask_jwt import JWT
from env import app_secret, is_debug

from resources.publication import Publication, PublicationList
from resources.user import UserRegister
from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = app_secret

# db configuration
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

# auth configuration
jwt = JWT(app,authenticate,identity)

# endpoints configuration
api = Api(app)
api.add_resource(Publication, '/publication/<id>')
api.add_resource(PublicationList, '/publications')
api.add_resource(Healthcheck, '/healthcheck')
api.add_resource(Rubric, '/rubric/<id>')
api.add_resource(RubricList, '/rubrics')
api.add_resource(UserRegister, '/register')
api.add_resource(Like, '/like')

app.run(port=5000, debug=is_debug)