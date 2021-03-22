from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, caminho):
        try:
            result = []
            if not caminho.endswith(".csv"):
                raise ValueError("Arquivo inválido")
            with open(caminho) as file:
                reader = csv.DictReader(file, delimiter=',')
                for line in reader:
                    result.append(dict(line))
                return result
        except FileNotFoundError:
            raise ValueError("Arquivo não encontrado")
