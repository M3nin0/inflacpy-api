class Util():
    @staticmethod
    def corr_date_input(inpt):
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
