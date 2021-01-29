from inventory_report.reports.simple_report import SimpleReport
from collections import Counter

class CompleteReport(SimpleReport):

    @classmethod
    def generate(cls, data):
       #primeiro salva o siple report no result
       result = super().generate(data)
       result += "Produtos estocados por empresa:\n"

       #agora gera o restante do relatório
       for info in data:
         EmpresaCount = Counter(simpleData["nome_da_empresa"] for simpleData in data)
         
       result += EmpresaCount

       return result
