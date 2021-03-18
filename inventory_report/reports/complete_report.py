from inventory_report.reports.simple_report import SimpleReport
from collections import defaultdict


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, dict_list):
        results = super().generate(dict_list)
        company_count = defaultdict(lambda: 0)

        for report in dict_list:
            company_count[report["nome_da_empresa"]] += 1

        results += "\nProdutos estocados por empresa: \n"

        for name in company_count:
            results += f"- {name}: {company_count[name]}\n"

        return results
