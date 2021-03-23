from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, stock):
        heritaged_report = super().generate(stock)
        # heritaged_report = super(CompleteReport, self).generate(stock)

        companys_by_name = [data["nome_da_empresa"] for data in stock]

        c = Counter(companys_by_name)

        company_by_qty = []

        for x in c:
            company_by_qty.append(f"- {x}: {c[x]}\n")

        company_by_qty_str = "".join(map(str, company_by_qty))

        formated_str = (
            f"{heritaged_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{company_by_qty_str}"
        )

        return formated_str
