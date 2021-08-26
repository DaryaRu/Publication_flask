from flask import Flask
from flask_restful import Api
from resources.healthcheck import Healthcheck

app = Flask(__name__)
api = Api(app)

api.add_resource(Healthcheck, '/healthcheck')

app.run(port=5000, debug=True)