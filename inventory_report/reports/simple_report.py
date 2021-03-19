from datetime import date
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, list_dict):
        today = date.today().strftime("%Y-%m-%d")
        oldest_date = min([old['data_de_fabricacao'] for old in list_dict])
        newest_date = min([
          x['data_de_validade'] for x in list_dict
          if x['data_de_validade'] > today
        ])
        company = max(
          Counter([index['nome_da_empresa'] for index in list_dict])
          )

        return (
          f"Data de fabricação mais antiga: {oldest_date}\n"
          f"Data de validade mais próxima: {newest_date}\n"
          f"Empresa com maior quantidade de produtos estocados: {company}\n"
        )
