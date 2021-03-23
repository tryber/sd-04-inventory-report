from datetime import datetime
from collections import Counter


'''Receber dados tipo dict e retornar uma string como um relatório'''


class SimpleReport:
    '''criar métodos que pertençam à classe'''
    @classmethod
    def generate(cls, data):
        '''qtd = empresa com maior quantidade de produtos estocados'''
        qtd = max(Counter(produto["nome_da_empresa"] for produto in data))

        fabricacao = min([produto["data_de_fabricacao"] for produto in data])

        validade = min([
            produto["data_de_validade"] for produto in data
            if datetime.now()
            < datetime.strptime(produto["data_de_validade"], '%Y-%m-%d')
        ])

        return (
            f"Data de fabricação mais antiga: {fabricacao}\n"
            f"Data de validade mais próxima: {validade}\n"
            f"Empresa com maior quantidade de produtos estocados: {qtd}\n"
        )
