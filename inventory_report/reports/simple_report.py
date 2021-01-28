# https://www.edureka.co/community/17742/in-list-of-dicts-find-min-value-of-a-common-dict-field
# https://www.programiz.com/python-programming/datetime/current-datetime
# https://stackoverflow.com/questions/15815976/group-count-list-of-dictionaries-based-on-value


from datetime import date
from collections import Counter


class SimpleReport:
    def __init__(self):
        self = self

    def generate(data):
        today = date.today().isoformat()
        oldest_fab_date = min([x["data_de_fabricacao"] for x in data])
        nearest_exp_date = min(
            [
                y["data_de_validade"]
                for y in data
                if y["data_de_validade"] > today
            ]
        )

        empr = max(Counter(emp["nome_da_empresa"] for emp in data))

        return (
            f"Data de fabricação mais antiga: {oldest_fab_date}\n"
            + f"Data de validade mais próxima: {nearest_exp_date}\n"
            + f"Empresa com maior quantidade de produtos estocados: {empr}\n"
        )


# print(SimpleReport.generate(data))

# map: [x["data_de_fabricacao"] for x in data]
# filter: ...map if condição
