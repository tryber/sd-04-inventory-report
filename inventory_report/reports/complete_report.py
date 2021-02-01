from inventory_report.reports.simple_report import SimpleReport
# from datetime import datetime


class CompleteReport(SimpleReport):
    def __init__(self, report):
        self.report = report

    @classmethod
    def generate(cls, report):
        simple_report = super().generate(report)
        count_company_occurrence = super().count_company_occurrence(report)

        def stock_by_company():
            for key in count_company_occurrence.keys():
                print(f"- {key}: {count_company_occurrence[key]}")

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:",
            stock_by_company()
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
