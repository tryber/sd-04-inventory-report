from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list_dict):
        simple_report = super().generate(list_dict)
        qtd_products = Counter(
            [index["nome_da_empresa"] for index in list_dict]
        )
        product_stocked = "Produtos estocados por empresa: \n"

        for key, value in qtd_products.items():
            product_stocked += f"- {key}: {value}\n"

        return f"{simple_report}\n{product_stocked}"
