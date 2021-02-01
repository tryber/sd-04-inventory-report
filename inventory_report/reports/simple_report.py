from datetime import date
from collections import Counter


class SimpleReport:
    @classmethod
    def __init__(self):
        self = self

    def generate(data):
        today = date.today().isoformat()

        dataFabr = min(
            [simpleData["data_de_fabricacao"] for simpleData in data]
        )
        dataValid = min(
            [
                simpleData["data_de_validade"]
                for simpleData in data
                if simpleData["data_de_validade"] > today
            ]
        )
        Emp = max(
            Counter(simpleData["nome_da_empresa"] for simpleData in data)
        )

        return (
            f"Data de fabricação mais antiga: {dataFabr}\n"
            + f"Data de validade mais próxima: {dataValid}\n"
            + f"Empresa com maior quantidade de produtos estocados: {Emp}\n"
        )
