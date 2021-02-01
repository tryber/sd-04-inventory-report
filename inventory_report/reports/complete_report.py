from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self):
        self = self

    @classmethod
    def generate(cls, report):
        simple_report = super().generate(report)
        count_company_occurrence = super().count_company_occurrence(report)

        company_list = "Produtos estocados por empresa: \n"
        for key in count_company_occurrence.keys():
            company_list += f"- {key}: {count_company_occurrence[key]}\n"
        return f"{simple_report}" "\n" f"{company_list}"
