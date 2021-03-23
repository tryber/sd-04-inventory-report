from datetime import datetime
from statistics import mode


class SimpleReport:
    def __init__(self):
        pass

    @classmethod
    def generate(self, stock):
        today_day = datetime.today()
        day_formated = f"{today_day.year}-0{today_day.month}-{today_day.day}"

        fab_day = min(
            [
                datetime.strptime(
                    data["data_de_fabricacao"], "%Y-%m-%d"
                ).date()
                for data in stock
            ]
        )

        # cria a string de data
        # // https://www.programiz.com/python-programming/datetime/strptime

        val_date = min(
            [
                datetime.strptime(data["data_de_validade"], "%Y-%m-%d").date()
                for data in stock
                if datetime.strptime(
                    data["data_de_validade"], "%Y-%m-%d"
                ).date()
                > datetime.strptime(day_formated, "%Y-%m-%d").date()
            ]
        )

        stocked = mode([data["nome_da_empresa"] for data in stock])
        # função mode serve para encontrar valor mais frequente

        brief = (
            f"Data de fabricação mais antiga: {fab_day}\n"
            f"Data de validade mais próxima: {val_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {stocked}\n"
        )

        return brief
