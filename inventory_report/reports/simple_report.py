from datetime import datetime


class SimpleReport:
    def __init__(self, report):

        self.report = report

    def generate(self):
        def list_companies():
            company_list = []
            for products in self.report:
                if products["nome_da_empresa"] not in company_list:
                    company_list.append(products["nome_da_empresa"])
            number_companies = []
            for company in company_list:
                counter = 0
                for products in self.report:
                    if products["nome_da_empresa"] == company:
                        counter += 1
                number_companies.append({company: counter})
            return number_companies

        def expiry_date():
            expiry_list = [x["data_de_validade"] for x in self.report]
            list_of_dates = [
                datetime.strptime(date, "%Y-%m-%d") for date in expiry_list
            ]
            return max(list_of_dates)

        def fabrication_date():
            fabrication_list = [x["data_de_fabricacao"] for x in self.report]
            list_of_dates = [
                datetime.strptime(date, "%Y-%m-%d")
                for date in fabrication_list
            ]
            return min(list_of_dates)

        company = list_companies()
        expiry = expiry_date()
        fabrication = fabrication_date()
        print(company, expiry, fabrication)


teste = [
    {
        "nome_da_empresa": "Ford",
        "data_de_fabricacao": "2020-01-13",
        "data_de_validade": "2020-01-15",
    },
    {
        "nome_da_empresa": "Fiat",
        "data_de_fabricacao": "2001-01-13",
        "data_de_validade": "2020-03-20",
    },
    {
        "nome_da_empresa": "Ford",
        "data_de_fabricacao": "2000-12-01",
        "data_de_validade": "2020-01-15",
    },
]
classe_teste = SimpleReport(teste)

classe_teste.generate()
