import datetime
from collections import Counter


class SimpleReport:
    def __init__(self):
        self = self

    def generate(data):
        hoje = datetime.date.today().isoformat()
        data_mais_antiga = min([item["data_de_fabricacao"] for item in data])
        data_mais_proxima = min([
          item["data_de_validade"]
          for item in data
          if item["data_de_validade"] > hoje
        ])
        empresa = max(Counter(empresa["nome_da_empresa"] for empresa in data))

        return (
            f"Data de fabricação mais antiga: {data_mais_antiga}\n"
            f"Data de validade mais próxima: {data_mais_proxima}\n"
            f"Empresa com maior quantidade de produtos estocados: {empresa}\n"
        )
