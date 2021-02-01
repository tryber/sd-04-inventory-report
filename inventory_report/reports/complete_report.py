from inventory_report.reports.simple_report import SimpleReport

# from datetime import datetime


class CompleteReport(SimpleReport):
    def __init__(self, report):
        self.report = report

    @classmethod
    def generate(cls, report):

        # def get_min_date(dates_list):
        #     datetimes_list = [
        #         datetime.strptime(date, "%Y-%m-%d")
        #         for date in dates_list
        #     ]
        #     get_min = min(datetimes_list)
        #     return get_min.strftime("%Y-%m-%d")

        # def oldest_manufacturing_date():
        #     fabrication_list = [x["data_de_fabricacao"] for x in report]
        #     return get_min_date(fabrication_list)

        # def closest_expiration_date():
        #     today = datetime.strftime(datetime.now(), "%Y-%m-%d")
        #     expiration_date_list = [
        #         x["data_de_validade"] for x in report
        #         if x["data_de_validade"] > today
        #     ]
        #     return get_min_date(expiration_date_list)

        # def max_company_occurrence():
        #     companies_list = [x["nome_da_empresa"] for x in report]
        #     count_companies = {
        #         i: companies_list.count(i) for i in companies_list
        #     }
        #     max_company_value = max(count_companies, key=count_companies.get)
        #     return max_company_value

        simple_report = SimpleReport.generate(report)
        get_simple_data = SimpleReport.generate(report).count_occurrence
        # manufacturing = oldest_manufacturing_date()
        # expiration = closest_expiration_date()
        # company = max_company_occurrence()

        print(
            f"{simple_report}\n"
            f"{get_simple_data}\n"
            f"Produtos estocados por empresa:\n"
            # f"- {EMPRESA}: {QUANTIDADE}\n"
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
classe_teste = CompleteReport(teste)

classe_teste.generate(teste)
