from datetime import date


class SimpleReport:
    def __init__(self):
        self = self

    @classmethod
    def count_company_occurrence(cls, report):
        companies_list = [x["nome_da_empresa"] for x in report]
        count_items = {i: companies_list.count(i) for i in companies_list}
        return count_items

    @classmethod
    def generate(cls, report):
        # Getting Oldest Fabrication Date
        min_fabrication = min([x["data_de_fabricacao"] for x in report])
        # Getting Closest Expiration Date
        today = date.today().isoformat()
        min_expiration_date = min(
            [
                x["data_de_validade"]
                for x in report
                if x["data_de_validade"] > today
            ]
        )
        # Getting company with highest number of products
        count_companies = cls.count_company_occurrence(report)
        company = max(count_companies, key=count_companies.get)

        return (
            f"Data de fabricação mais antiga: {min_fabrication}\n"
            f"Data de validade mais próxima: {min_expiration_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {company}\n"
        )


teste = [
    {
        "nome_da_empresa": "Ford",
        "data_de_fabricacao": "2020-01-13",
        "data_de_validade": "2020-01-15",
    },
    {
        "nome_da_empresa": "Fiat",
        "data_de_fabricacao": "2001-01-13",
        "data_de_validade": "2021-03-20",
    },
    {
        "nome_da_empresa": "Ford",
        "data_de_fabricacao": "2000-12-01",
        "data_de_validade": "2022-01-15",
    },
]


SimpleReport.generate(teste)
