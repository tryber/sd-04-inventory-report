import statistics
from collections import Counter
from datetime import datetime

lista = [
    {
        "id": 1,
        "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2020-07-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
        "instrucoes_de_armazenamento": "in blandit ultrices enim",
    },
    {
        "id": 2,
        "nome_do_produto": "sodium ferric gluconate complex",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2020-05-31",
        "data_de_validade": "2023-01-17",
        "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
        "instrucoes_de_armazenamento": "duis bibendum morbi",
    },
    {
        "id": 3,
        "nome_do_produto": "Dexamethasone Sodium Phosphate",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2019-09-13",
        "data_de_validade": "2023-02-13",
        "numero_de_serie": "BA52 2034 8595 7904 7131",
        "instrucoes_de_armazenamento": "morbi quis tortor id",
    },
    {
        "id": 4,
        "nome_do_produto": "Uricum acidum, Benzoicum acidum",
        "nome_da_empresa": "Newton Laboratories, Inc.",
        "data_de_fabricacao": "2019-11-08",
        "data_de_validade": "2019-11-25",
        "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
        "instrucoes_de_armazenamento": "velit eu est congue elementum",
    },
]


class CompleteReport:
    @classmethod
    def generate(cls, lista):
        date_now = datetime.today().strftime("%Y-%m-%d")
        fab_date_list = []
        val_date_list = []
        name_list = []
        res = []
        quantity_list = []
        for item in lista:
            fab_date_list.append(item["data_de_fabricacao"])
            val_date_list.append(item["data_de_validade"])
            name_list.append(item["nome_da_empresa"])
        for val in val_date_list:
            if val > date_now:
                res.append(val)
        company = statistics.mode(name_list)
        quantity = Counter(name_list)

        for item, quant in quantity.items():
            quantity_list.append(f"- {item}: {quant}")

        report_quantity = '\n'.join(quantity_list)

        report = (
            f"Data de fabricação mais antiga: {min(fab_date_list)}\n"
            f"Data de validade mais próxima: {min(res)}\n"
            f"Empresa com maior quantidade de produtos "
            f"estocados: {company}\n\n"
            "Produtos estocados por empresa: \n"
            f"{report_quantity}\n"
            )

        print(report)
        return report


CompleteReport.generate(lista)
