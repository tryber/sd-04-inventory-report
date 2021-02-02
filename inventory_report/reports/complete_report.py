from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        simple_report = super().generate(data)
        qntd_product = Counter([
            product["nome_da_empresa"]
            for product in data
        ])

        company_products = "\nProdutos estocados por empresa: \n"

        for company in qntd_product.items():
            company_products += f"- {company[0]}: {company[1]}\n"
        complete_report = simple_report + company_products

        return complete_report
