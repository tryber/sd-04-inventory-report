from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


''' '''


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        simple_report = super().generate(data)
        emp_estoque = "\nProdutos estocados por empresa: \n"
        qtd = Counter([
            produto["nome_da_empresa"]
            for produto in data
        ])

        for emp in qtd.items():
            emp_estoque += f"- {emp[0]}: {emp[1]}\n"
        completeReport = simple_report + emp_estoque

        return completeReport
