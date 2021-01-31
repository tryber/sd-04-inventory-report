from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, data):
        fabrication = min([product["data_de_fabricacao"] for product in data])

        validation = min([
            product["data_de_validade"] for product in data
            if datetime.now()
            < datetime.strptime(product["data_de_validade"], '%Y-%m-%d')
        ])

        company = max(Counter(product["nome_da_empresa"] for product in data))

        return (
            f"Data de fabricação mais antiga: {fabrication}\n"
            f"Data de validade mais próxima: {validation}\n"
            f"Empresa com maior quantidade de produtos estocados: {company}\n"
        )
