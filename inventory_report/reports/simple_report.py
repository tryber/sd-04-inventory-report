from datetime import datetime
from collections import Counter


class SimpleReport:
    def __init__(self):
        self = self

    @classmethod
    def generate(cls, lista):
        data_e_hora_atuais = datetime.now()
        date_time = data_e_hora_atuais.strftime("%Y/%m/%d")
        data_mais_antiga = min(
            [produto["data_de_fabricacao"]
                for produto in lista]
        )
        data_validade_proxima = min(
            [produto["data_de_validade"] for produto in lista
                if produto["data_de_validade"] > date_time]
        )
        estoque = max(
            Counter(
                [produto["nome_da_empresa"]
                    for produto in lista])
        )
        return (
            f"Data de fabricação mais antiga: {data_mais_antiga}\n"
            f"Data de validade mais próxima: {data_validade_proxima}\n"
            f"Empresa com maior quantidade de produtos estocados: {estoque}\n"
        )
