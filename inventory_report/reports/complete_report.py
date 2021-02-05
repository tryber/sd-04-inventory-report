import collections
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        res_simple_report = super().generate(data)
        quantity_products = collections.Counter(
            [stock["nome_da_empresa"] for stock in data]
        )

        stocked_products = "\nProdutos estocados por empresa: \n"

        for company in quantity_products:
            stocked_products += f"- {company}: {quantity_products[company]}\n"
            response = res_simple_report + stocked_products

        return response
