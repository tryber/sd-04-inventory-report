import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def __init__(self):
        pass
        # self.simple = SimpleReport()
        # self.complete = CompleteReport()

    @classmethod
    def simple_complete(cls, stock, tipe):
        if tipe == 'simples':
            return SimpleReport.generate(stock)
        else:
            return CompleteReport.generate(stock)

    @classmethod
    def import_data(cls, filepath, tipe):
        if filepath.endswith('.csv'):
            dado = cls.__csv_importer(filepath)
            return cls.simple_complete(dado, tipe)
        elif filepath.endswith('.json'):
            dado = cls.__json_importer(filepath)
            return cls.simple_complete(dado, tipe)

    @staticmethod
    def __csv_importer(caminho):
        try:
            result = []
            if not caminho.endswith(".csv"):
                raise ValueError("Formato invalido")
            with open(caminho) as file:
                reader = csv.DictReader(file, delimiter=',')
                for line in reader:
                    result.append(dict(line))
                return result
        except FileNotFoundError:
            raise ValueError("Arquivo não encontrado")

    @staticmethod
    def __json_importer(caminho):
        try:
            if not caminho.endswith(".json"):
                raise ValueError("Formato invalido")
            with open(caminho) as file:
                data = file.read()
                data_json = json.loads(data)
                return data_json
        except FileNotFoundError:
            raise ValueError("Arquivo não encontrado")


# arg1 = 'inventory_report/data/inventory.csv'
# arg3 = 'inventory_report/data/inventory.json'
# arg2 = 'simples'
# arg4 = 'completo'


# def teste(caminho, tipo):
#     a = Inventory()
#     return a.import_data(caminho, tipo)


# print(teste(arg3, arg4))
