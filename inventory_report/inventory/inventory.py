import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    # def __init__(self, report_result)

    @classmethod
    def import_data(cls, imported_file, report_type):
        cls.report_result = ""
        with open(imported_file) as file:
            file_reader = csv.reader(file, delimiter=",")
            header, *data = file_reader
            file_result = [
                {header: data for header, data in zip(header, data)}
                for data in data
            ]
            if report_type == "simples":
                cls.report_result = SimpleReport.generate(file_result)
            elif report_type == "completo":
                cls.report_result = CompleteReport.generate(file_result)
            else:
                cls.report_result = "Tipo de relatório inválido"
            file.close()
        return cls.report_result


# Inventory.import_data("inventory_report/data/inventory.csv", "completo")
