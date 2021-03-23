from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        simple_report = super().generate(list)
        print(simple_report)

        companies = [dict["nome_da_empresa"] for dict in list]
        products = Counter(companies)
        print(products)

        complete_report = "Produtos estocados por empresa: \n"
        for key, value in products.items():
            complete_report += f"- {key}: {value}\n"
        return f"{simple_report}\n{complete_report}"
