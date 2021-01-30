import datetime
from collections import Counter

"""
with open('../data/inventory.json', 'r') as file:
    content = file.read()
    data = json.loads(content)


company_name = []

for test in data:
    company_name.append(test['nome_da_empresa'])

print(company_name)
company_great_than_qtd = Counter(company_name)
print(company_great_than_qtd)
"""

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
        print('\ncompany_great_than_qtd:', company_great_than_qtd)
        print('company_great_than_qtd2:', max(company_great_than_qtd))

        simple_report = (
            f"Data de fabricação mais antiga: {min(manufacture_date)}\n"
            f"Data de validade mais próxima: {min(validity_prox_Date)}\n"
            f"Empresa com maior quantidade de produtos estocados: {max(company_great_than_qtd)}\n"
        )

        return simple_report
