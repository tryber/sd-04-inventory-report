from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(data):
        simple_report = SimpleReport.generate(data)

        empresa_quantidade = dict(
            list(Counter(item["nome_da_empresa"] for item in data).items())
        )

        dados_formatados = []

        for key in empresa_quantidade:
            dados_formatados.append(f"- {key}: {empresa_quantidade[key]}")

        strings = "\n".join(dados_formatados)

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{strings}\n"
        )
