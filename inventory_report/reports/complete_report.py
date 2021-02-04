from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, dict_list):
        simple_report = super().generate(dict_list)
        companies_names = [x["nome_da_empresa"] for x in dict_list]
        companies_products = Counter(companies_names)
        complete_report = "Produtos estocados por empresa: \n"
        for key, value in companies_products.items():
            complete_report += f"- {key}: {value}\n"
        return f"{simple_report}\n{complete_report}"
