import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def csv_importer(caminho):
    try:
        result = []
        if not caminho.endswith(".csv"):
            raise ValueError("Formato invalido")
        with open(caminho) as file:
            data = csv.DictReader(file, delimiter=',')
            result.append(data)
            return result
    except FileNotFoundError:
        raise ValueError("Arquivo não encontrado")


class Inventory:
    # fiz esse metodo pq minha intencao eh que ele se repita nos
    # tres requisitos pra cada tipo de arquivo
    def simple_complete(self, data, tipe):
        if tipe == 'simples':
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)

    def import_data(self, filepath, tipe):
        dado = csv_importer(filepath)
        self.simple_complete(dado, tipe)
        # if filepath.endswith('.csv'):
        #     with open(filepath) as file:
        #         print(f"filepath {filepath}")
        #         print(f"tipe {tipe}")
        #         data = [csv.DictReader(file, delimiter=",")]
        #         print(f"data {data}")
        #         self.simple_complete(data, tipe)

        # elif filepath.endswith('.json'):
        #     with open(filepath) as file:
        #         data = file.read()
        #         data_json = json.loads(data)
        #         self.simple_complete(data_json, tipe)

        # elif filepath.endswith('.xml'):
        #     with open(filepath) as file:
        #         data = file.read()
        #         simple_report(data, tipe)

        # else:


# arg1 = 'inventory_report/data/inventory.csv'
# arg2 = 'simples'

# n sei como faco pra testar essa coisa, achei q assim iria mas ele acusa erro
# dizendo que o segundo parametro n esta sendo passado


# def teste(a, b):
#     a = Inventory()
#     return a.import_data(a, b)


# print(teste(arg1, arg2))
