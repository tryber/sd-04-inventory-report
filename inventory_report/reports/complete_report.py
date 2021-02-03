from .simple_report import SimpleReport
from collections import Counter

class CompleteReport(SimpleReport):
  def generate(data):
        simple_report = SimpleReport.generate(data)

        empresas = Counter(empresa["nome_da_empresa"] for empresa in data)

        empresas_quant = "Produtos estocados por empresa: \n"

        for empresa in empresas:
            empresas_quant = (
                empresas_quant + f"- {empresa}: {empresas[empresa]}\n"
            )

        return f"{simple_report}" f"\n" f"{empresas_quant}"
