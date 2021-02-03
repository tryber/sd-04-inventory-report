from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, data):

        fmt = '%Y-%m-%d'
        now = datetime.now()

        old_fabrication = datetime.strptime(data[0]["data_de_fabricacao"], fmt)

        for product in data:
            date = product["data_de_fabricacao"]
            current_date = datetime.strptime(date, fmt)
            if current_date < old_fabrication:
                old_fabrication = current_date

        old_fabrication = old_fabrication.strftime(fmt)
        closest_validity = datetime.strptime(data[0]["data_de_validade"], fmt)

        for product in data:
            date = product["data_de_validade"]
            current_date = datetime.strptime(date, fmt)
            if (current_date < closest_validity) and (current_date > now):
                closest_validity = current_date

        closest_validity = closest_validity.strftime(fmt)

        lg_stock = max(Counter(product["nome_da_empresa"] for product in data))

        return (
            f"Data de fabricação mais antiga: {old_fabrication}\n"
            f"Data de validade mais próxima: {closest_validity}\n"
            f"Empresa com maior quantidade de produtos estocados: {lg_stock}\n"
        )
        