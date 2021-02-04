from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path_file):
        if path_file.endswith('.csv'):
            with open(path_file) as path_csv:
                reader_csv = csv.DictReader(path_csv, delimiter=',', quotechar='"')
                return list(reader_csv)
        else:
            return ValueError('Arquivo inválido')
