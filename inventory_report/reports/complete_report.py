from inventory_report.reports.simple_report import SimpleReport
from collections import defaultdict


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, dict_list):
        result = super().generate(dict_list)
        company_count = defaultdict(lambda: 0)

        for report in dict_list:
            company_count[report["nome_da_empresa"]] += 1

        result += "\nProdutos estocados por empresa: \n"

        for name in company_count:
            result += f"- {name}: {company_count[name]}\n"

        return result
