from inventory_report.importer.importer import Importer
import csv

class CsvImporter(Importer):
    
    def import_data(path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            data = []
            csv_reader = csv.DictReader(file)
            for item in csv_reader:
                data.append(item)
            return data
