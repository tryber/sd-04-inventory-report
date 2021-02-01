from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self, stock):
        self.stock = stock

    # def generate(self):
    #     return SimpleReport.generate(self)
    #      SimpleReport.company_name
