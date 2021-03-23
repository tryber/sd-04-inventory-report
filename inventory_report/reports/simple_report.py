from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, list):
        today_date = datetime.now().strftime("%Y-%m-%d")

        old_manufact = min([dict["data_de_fabricacao"] for dict in list])

        closest_expiration = min(
            [
                dict["data_de_validade"]
                for dict in list
                if dict["data_de_validade"] > today_date
            ]
        )

        company_stock = max(
            Counter([index["nome_da_empresa"] for index in list])
        )
        return f"""Data de fabricação mais antiga: {old_manufact}
Data de validade mais próxima: {closest_expiration}
Empresa com maior quantidade de produtos estocados: {company_stock}
"""
