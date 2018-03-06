from flask import Flask
from flask import request
from flask_restful import Api
from flask import render_template
from routes.routes import Inflation
from sqlalchemy import create_engine

app = Flask(__name__)
api = Api(app)

api.add_resource(Inflation, '/inflaction/<country>/<date_initial>/<date_final>/')

@app.route('/')
def teste():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
