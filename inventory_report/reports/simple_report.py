import datetime
from collections import Counter


class SimpleReport:
    def __init__(self, stock):
        self.stock = stock

    def generate(self):
        stock = self

        today = datetime.date.today()

        manufacture_date = []
        validity_date = []
        company_name = []
        for product in stock:
            manufacture_date.append(product['data_de_fabricacao'])
            validity_date.append(product['data_de_validade'])
            company_name.append(product['nome_da_empresa'])

        validity_prox_Date = []
        for validity in validity_date:
            proxValidity = datetime.date.fromisoformat(validity)
            if proxValidity > today:
                validity_prox_Date.append(validity)

        company_great_than_qtd = Counter(company_name)

        simple_report = (
            f"Data de fabricação mais antiga: {min(manufacture_date)}\n"
            f"Data de validade mais próxima: {min(validity_prox_Date)}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{max(company_great_than_qtd)}\n"
        )

        return simple_report
