import collections as col
from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, source):
        oldest_fab_date = min(
            [product["data_de_fabricacao"] for product in source]
        )

        closer_to_due = min(
            [
                product["data_de_validade"]
                for product in source
                if datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
                >= datetime.now()
            ]
        )

        largest_stock = max(
            col.Counter([product["nome_da_empresa"] for product in source])
        )

        return (
            f"Data de fabricação mais antiga: {oldest_fab_date}\n"
            f"Data de validade mais próxima: {closer_to_due}\n"
            f"Empresa com maior quantidade de produtos estocados: {largest_stock}\n"
        )
