from flask import Flask
from flask_restful import Api
from resources.healthcheck import Healthcheck
from db import db

from resources.publication import Publication, PublicationList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Publication, '/publication/<id>')
api.add_resource(PublicationList, '/publications')
api.add_resource(Healthcheck, '/healthcheck')

app.run(port=5000, debug=True)