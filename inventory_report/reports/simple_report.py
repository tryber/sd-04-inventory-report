from datetime import date
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, list_dict):
        today = date.today().strftime("%Y-%m-%d")
        old_fab_date = min([old['data_de_fabricacao'] for old in list_dict])
        new_fab_date = min([x['data_de_validade'] for x in list_dict if x['data_de_validade'] > today])
        company = max(Counter([index["nome_da_empresa"] for index in list_dict]))

        return (
            f"Data de fabricação mais antiga: {old_fab_date}\n"
            f"Data de validade mais próxima: {new_fab_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {company}\n"
            )
