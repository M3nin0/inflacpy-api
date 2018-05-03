def corr_date_input(inpt: str) -> str:
    '''
        Trata a string, removendo espaços e caracteres especiais
        :param: inpt: (str) Nome da cidade de entrada
        :rtype: String tratada
    '''
    inpt = inpt.lower()
    inpt = inpt.replace(' ', '-')
    inpt = inpt.replace('ç', 'c')
    inpt = inpt.replace('ã', 'a')

    return inpt


def corr_return_number(inpt: str) -> str:
    """Método para realizar correções nos valores retornados na raspagem
    """
    inpt = inpt \
        .replace('\xa0%', '') \
        .replace('\xa0%\xa0', '') \
        .replace('<td align="right">', '') \
        .replace('</td>', '') \
        .replace(',', '.') \
        .replace('\xa0', '') \
        .replace('%', '')

    # Verificando valores com multiplos pontos
    if inpt.count('.') == 2:
        inpt = inpt[0:-3]

    return inpt
