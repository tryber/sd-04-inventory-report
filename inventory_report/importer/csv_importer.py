from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(self, file_path):
        try:
            data = []
            if not file_path.endswith('.csv'):
                raise ValueError("Arquivo inválido")
            with open(file_path) as file:
                reader = csv.DictReader(file, delimiter=',')
                for item in reader:
                    data.append(dict(item))
                return data
        except FileNotFoundError:
            raise ValueError('Arquivo não encontrado')