
from api import app

from json import dumps
from flask import request
from flask import render_template
from flask_restful import Resource
from flask.ext.jsonpify import jsonify

from api.models.inflacpy.scrap.scrap import Scrap

scrap = Scrap()

@app.route('/')
def home():
    """Método para retorno da página inicial
    """
    return render_template('index.html')

@app.route('/search')
def get():
    """Método de busca de países
    """

    initial_date = request.args.get('initial')
    final_date = request.args.get('final')
    country = request.args.get('country')
    
    try:
        return jsonify(scrap.get_data(year_start=int(initial_date), year_end=int(final_date), country=country))
    except:
        return jsonify('Insira todos os campos')
