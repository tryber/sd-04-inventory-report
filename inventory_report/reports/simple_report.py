import datetime
from collections import Counter


class SimpleReport:
    def __init__(self, stock):
        self.stock = stock

    def generate(self):
        stock = self

        # compara a chave data_de_fabricacao de todos os objetos para encontrar a mais antiga
        manufacture_date = []
        validation_date = []
        company_name = []
        for product in stock:
            manufacture_date.append(product['data_de_fabricacao'])
            validation_date.append(product['data_de_validade'])
            company_name.append(product['nome_da_empresa'])

        company_great_than_qtd = Counter(company_name)
        print('manufacture_date:', min(manufacture_date))
        print('validation_date:', validation_date)
        print('company_great_than_qtd:', company_great_than_qtd)
        simple_report = (
            f"Data de fabricação mais antiga: {min(manufacture_date)}\n"
            f"Data de validade mais próxima: {max(validation_date)}\n"
            f"Empresa com maior quantidade de produtos estocados: {company_great_than_qtd[0]}"
        )

        return simple_report
