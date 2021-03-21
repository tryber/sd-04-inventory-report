from inventory_report.reports.simple_report import SimpleReport
import collections as col


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, source):
        simple_report = super().generate(source)

        qnt_products_by_company = col.Counter(
            [product["nome_da_empresa"] for product in source]
        )

        companys_quantity_report = ''
        for company in qnt_products_by_company:
            companys_quantity_report += (
                f"- {company}: {qnt_products_by_company[company]}\n"
            )

        return (
            f"{simple_report}"
            f"\nProdutos estocados por empresa: \n"
            f"{companys_quantity_report}"
        )
