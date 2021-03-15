from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, lista):
        simple_report = super().generate(lista)
        qntd_produtos = Counter([
            produto["nome_da_empresa"]
            for produto in lista
        ])

        complete_report = "Produtos estocados por empresa: \n"

        for key, value in qntd_produtos.items():
            complete_report += f"- {key}: {value}\n"

        return (
            f"{simple_report}\n{complete_report}"
        )
