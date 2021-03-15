from inventory_report.reports.simple_report import SimpleReport
from collections import defaultdict


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, dict_list):
        result = super().generate(dict_list)
        company_total = defaultdict(lambda: 0)

        for report in dict_list:
            company_total[report["nome_da_empresa"]] += 1

        result += "\nProdutos estocados por empresa: \n"

        for company in company_total:
            result += f"- {company}: {company_total[company]}\n"

        return result
