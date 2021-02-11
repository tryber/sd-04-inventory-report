from datetime import datetime
from collections import Counter


class SimpleReport:
    def __init__(self):
        return self

    def generate(data):
        today = datetime.today()
        oldest_mfg_date = min([
            datetime.strptime(product["data_de_fabricacao"], "%Y-%m-%d").date()
            for product in data
        ])
        future_dates = []
        for product in data:
            d = datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
            if d > today:
                future_dates.append(d.date())
        closest_exp_date = min([
            product
            for product in future_dates
        ])
        company_name = Counter([
            product["nome_da_empresa"] for product in data
        ]).most_common(1)[0]

        return(
            f"Data de fabricação mais antiga: {oldest_mfg_date}\n" +
            f"Data de validade mais próxima: {closest_exp_date}\n" +
            "Empresa com maior quantidade de produtos estocados:"
            f" {company_name[0]}\n"
            )
