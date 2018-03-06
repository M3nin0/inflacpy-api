import requests
import datetime
from bs4 import BeautifulSoup

from inflacpy.utils.utils import Util

class Scrap():
    '''
        Classe do scraper
    '''

    def __init__(self):
        self.url = 'http://pt.inflation.eu/taxas-de-inflacao/brasil/inflacao-historica/'


    def get_data(self, year_start=1981, year_end=0, country=''):
        '''
            Método para recuperar os dados da inflação

            :param: year_start: (str) Ano inicial das pesquisas de inflação
            :param: year_end: (str) Ano limite para as pesquisas de inflação
            :param: country: (str) Nome do país a ser pesquisado
            :rtype: list
        '''

        now = datetime.datetime.now()
        country = Util.corr_date_input(country)
        links_anos = []

        # Caso o usuário não tenha inserido o ano limite
        if year_end == 0:
            year_end = now.year

        self.url += 'ipc-inflacao-' + country + '-'

        for year in range(year_start, year_end + 1):
            links_anos.append(self.url + str(year) + '.aspx')

        inflacoes = []
        # Recuperando as informações de todos os links
        for link in links_anos:
            ano = link[87:91]
            r = requests.get(link)
            soup = BeautifulSoup(r.text, 'html.parser')

            inflacoes.append(dict())
            inflacoes[0][ano] = {}
            inflacoes[0][ano]['mensal'] = []
            inflacoes[0][ano]['anual'] = []
            for mes in range(0, 6):

                # Filtra a classe das tabelas - Mensais e anuais
                tabledata1 = soup.findAll('tr', {'class': 'tabledata1'})
                tabledata2 = soup.findAll('tr', {'class': 'tabledata2'})

                table_1 = tabledata1[mes].find_all('td')
                table_2 = tabledata2[mes].find_all('td')

                # Salvando os dados de maneira organizada
                for element_1 in table_1[1]:
                    for element_2 in table_2[1]:
                        inflacoes[0][ano]['mensal'].append(
                                str(element_1)\
                                    .replace('\xa0%\xa0', '')\
                                    .replace('<td align="right">', '')\
                                    .replace('</td>', '')\
                                    .replace(',','.')\
                                    .replace('\xa0', '')
                                    .replace('%', '')
                                )

                        inflacoes[0][ano]['mensal'].append(
                                str(element_2)\
                                    .replace('\xa0%', '')\
                                    .replace('<td align=\"right\">', '')\
                                    .replace('</td>', '')\
                                    .replace(',', '.')
                                    .replace('\xa0', '')
                                    .replace('%', '')
                                )

                for element_1 in table_1[4]:
                    for element_2 in table_2[4]:
                        inflacoes[0][ano]['anual'].append(
                                str(element_1)\
                                    .replace('\xa0%\xa0', '')\
                                    .replace('<td align="right">', '')\
                                    .replace('</td>', '')\
                                    .replace(',','.')\
                                    .replace('\xa0', '')
                                    .replace('%', '')
                                )

                        inflacoes[0][ano]['anual'].append(
                                str(element_2)\
                                    .replace('\xa0%', '')\
                                    .replace('<td align=\"right\">', '')\
                                    .replace('</td>', '')\
                                    .replace(',', '.')
                                    .replace('\xa0', '')
                                    .replace('%', ''))

        return inflacoes
