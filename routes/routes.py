from json import dumps
from flask_restful import Resource
from flask.ext.jsonpify import jsonify

from inflacpy.scrap.scrap import Scrap

scrap = Scrap()

class Inflation(Resource):
    '''
        Classe da busca de informações de inflação - em tempo real
    '''
    def get(self, country, date_initial, date_final):
        return jsonify(scrap.get_data(year_start=int(date_initial), year_end=int(date_final), country=country))
