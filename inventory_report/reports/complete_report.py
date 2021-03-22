from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products_list):
        simple_report = SimpleReport.generate(products_list)
        companies_total_products_dict = Counter(
            [product["nome_da_empresa"] for product in products_list]
        )

        companies_report = ""

        for company in companies_total_products_dict:
            companies_report += (
                f"- {company}: {companies_total_products_dict[company]}\n"
            )

        return f"""{simple_report}
Produtos estocados por empresa: 
{companies_report}"""
