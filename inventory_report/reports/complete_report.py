from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, data):
        simple_report = super().generate(data)

        stock = Counter([product["nome_da_empresa"] for product in data])

        new_return = "\nProdutos estocados por empresa: \n"

        for name_company in stock.items():
            new_return += f"- {name_company[0]}: {name_company[1]}\n"

        return simple_report + new_return
