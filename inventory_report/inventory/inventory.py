from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv

classes = {"simples": SimpleReport, "completo": CompleteReport}


class Inventory:
    @classmethod
    def import_data(self,filepath, report_type):
        if not filepath.endswith(".csv"):
            print("filepath", filepath)
            raise ValueError("Formato invalido")    

        try:
            file_opened = open(filepath, encoding="utf-8")
            file_read = csv.reader(file_opened, delimiter=";")
            header, *data = file_read
            file_output = []
            reader = csv.DictReader(open(filepath, encoding="utf-8"))
            for row in reader:
                temp_dict = {}
                for key, value in row.items():
                    temp_dict[key] = value
                file_output.append(temp_dict)
            # return file_output
            return classes[report_type].generate(file_output)
        except FileNotFoundError:
            raise ValueError("Arquivo tests/file_not_exist.csv não encontrado")
        else:
            print("arquivo manipulado e fechado com sucesso")
            file_opened.close()
        # return classes[report_type].generate(file_output)
        # finally:
