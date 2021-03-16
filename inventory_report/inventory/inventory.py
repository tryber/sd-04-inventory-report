from inventory_report.reports.simple_report import SimpleReport
import csv


class Inventory:
    @classmethod
    def import_data(cls, file_path, type):
        report = []
        if file_path.endswith(".csv"):
            report = cls.reader_csv(file_path)
        if type == "simples":
            return SimpleReport.generate(report)
        elif type == "completo":
            return 'arquivo Compelto'
    @classmethod
    def reader_csv(cls, file_path):
        with open(file_path) as file:
            csv_file = csv.DictReader(file, delimiter=",")
            return [row for row in csv_file]
