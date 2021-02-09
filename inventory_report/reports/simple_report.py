from collections import Counter
from operator import itemgetter
from datetime import date


class SimpleReport:
    @classmethod
    def greater_than_today(self, list_data):
        today = date.today()
        return list_data["data_de_validade"] >= today.strftime("%Y-%m-%d")

    @classmethod
    def generate(self, list_dict):
        oldest_date = min(list_dict, key=itemgetter("data_de_fabricacao"))["data_de_fabricacao"]
        not_expired = filter(self.greater_than_today, list_dict)
        nearest_date = min(not_expired, key=itemgetter("data_de_validade"))["data_de_validade"]
        counter_employees = Counter(product['nome_da_empresa'] for product in list_dict)
        most_product_employee = max(counter_employees, key=counter_employees.get)

        report = f"Data de fabricação mais antiga: {oldest_date}\n"
        report += f"Data de validade mais próxima: {nearest_date}\n"
        report += "Empresa com maior quantidade de produtos estocados:"
        report += f" {most_product_employee}\n"
        return report
