import json
import datetime


class SimpleReport:
    def __init__(self, stock):
        self.stock = stock

    def generate(self):
        stock = self

        # compara a chave data_de_fabricacao de todos os objetos para encontrar a mais antiga
        oldest_date = datetime.date.today()
        for product in stock:
            productDate = datetime.date.fromisoformat(product['data_de_fabricacao'])
            if productDate < oldest_date:
                oldest_date = productDate
        print("Data de fabricação mais antiga:", oldest_date)
        return f"Data de fabricação mais antiga: {oldest_date}"

        # compara a chave data_de_validade de todos os objetos para encontrar a mais próxima, que ainda não venceu
        # datetime - timedelta
        # print("Data de validade mais próxima: YYYY-MM-DD")

        # Utilizar a chave nome_da_empresa para contar a quantidade de produtos da empresa
        # Depois comparar esses valores para ver quem tem o maior número de produtos estocados.
        # print("Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA")
