from inventory_report.reports.simple_report import SimpleReport
from collections import defaultdict

class CompleteReport (SimpleReport) :
    def generate(data):
        result = SimpleReport.generate(data)
        entreprise_count = defaultdict(lambda: 0)

        for report in data:
            entreprise_count[report["nome_da_empresa"]] += 1

        result += "\nProdutos estocados por empresa: \n"

        for company in entreprise_count:
         result += f"- {company}: {entreprise_count[company]}\n"

        return result
