from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list_dict):
        simple_report = super().generate(list_dict)
        qtdd_products = Counter([
          index["nome_da_empresa"]
          for index in list_dict
        ])
        product_in_stock = "Produtos estocados por empresa: \n"

        for key, value in qtdd_products.items():
            product_in_stock += f"- {key}: {value}\n"

        return (
          f"{simple_report}\n{product_in_stock}"
        )
