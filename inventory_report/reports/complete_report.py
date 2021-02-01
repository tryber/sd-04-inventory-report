from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        # primeiro salva o siple report no result
        result = super().generate(data)
        result += "\nProdutos estocados por empresa: \n"
        # agora gera o restante do relatório
        EmpresaCount = Counter(
            simpleData["nome_da_empresa"] for simpleData in data
        )
        for i in EmpresaCount:
            result += f"- {i}: {EmpresaCount[i]}\n"
        return result
