from datetime import datetime
from statistics import mode


class SimpleReport:
    def __init__(self, files):
        self.files = files

    def generate(stock):

        hoje = datetime.today()
        formated_today = f"{hoje.year}-0{hoje.month}-{hoje.day}"

        datas_de_fabricacao = max(
            [
                datetime.strptime(
                    data["data_de_fabricacao"], "%Y-%m-%d"
                ).date()
                for data in stock
            ]
        )

        datas_de_validade = min(
            [
                datetime.strptime(data["data_de_validade"], "%Y-%m-%d").date()
                for data in stock
                if datetime.strptime(
                    data["data_de_validade"], "%Y-%m-%d"
                ).date()
                > datetime.strptime(formated_today, "%Y-%m-%d").date()
            ]
        )

        estocado = mode([data["nome_da_empresa"] for data in stock])

        relatorio = (
            f"Data de fabricação mais antiga: {datas_de_fabricacao}\n"
            f"Data de validade mais próxima: {datas_de_validade}\n"
            f"Empresa com maior quantidade de produtos estocados: {estocado}\n"
        )

        return relatorio
