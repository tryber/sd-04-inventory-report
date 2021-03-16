from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @classmethod
    def import_data(cls, file_path, type):
        report = []
        if file_path.endswith(".csv"):
            report = cls.reader_csv(file_path)
        elif file_path.endswith('.json'):
            report = cls.reader_json(file_path)
        if type == "simples":
            return SimpleReport.generate(report)
        elif type == "completo":
            return CompleteReport.generate(report)

    @classmethod
    def reader_csv(cls, file_path):
        with open(file_path) as file:
            csv_file = csv.DictReader(file, delimiter=",")
            return [row for row in csv_file]

    @classmethod
    def reader_json(cls, file_path):
        with open(file_path) as file:
            return json.load(file)
