from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list_dict):
        simple_report = super().gerate(list_dict)
        qtd_products = Counter([
            product["nome_da_empresa"]
            for product in list
        ])
        product_stocked = "Produtos estocados por empresa:\n"
        
        for key, value in qtd_products.items():
            product_stocked += f"- {key}: {value}\n"

        return (
            f"{simple_report}\n{complete_report}"
        )
