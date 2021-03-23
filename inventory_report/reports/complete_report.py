from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, stock):
        heritaged_generate = super().generate(stock)

        companys_name = [data["nome_da_empresa"] for data in stock]

        counter = Counter(companys_name)

        companys_quantity = []

        for x in counter:
            companys_quantity.append(f"- {x}: {counter[x]}\n")

        comp_str_qty = "".join(map(str, companys_quantity))

        formated_result = (
            f"{heritaged_generate}\n"
            f"Produtos estocados por empresa: \n"
            f"{comp_str_qty}"
        )

        return formated_result
