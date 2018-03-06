from flask import Flask
from flask import request
from flask_restful import Api
from routes.routes import Inflation
from sqlalchemy import create_engine

app = Flask(__name__)
api = Api(app)

api.add_resource(Inflation, '/inflaction/<country>/<date_initial>/<date_final>/')

if __name__ == '__main__':
    app.run()
