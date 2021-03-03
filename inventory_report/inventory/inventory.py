from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    @classmethod
    def import_data(cls, path, tipo):
        if path.endswith(".csv"):
            with open(path) as csv_file:
                data = []
                csv_reader = csv.DictReader(csv_file)
                for item in csv_reader:
                    data.append(item)
                if(tipo == 'simples'):
                    return SimpleReport.generate(data)
                else:
                    return CompleteReport.generate(data)
        elif path.endswith(".json"):
            with open(path, 'r') as json_file:
                data = json.load(json_file)
                if(tipo == 'simples'):
                    return SimpleReport.generate(data)
                else:
                    return CompleteReport.generate(data)
        else:
            root = ET.parse(path).getroot()
            data = []
            for child in root:
                obj = {}
                for neto in child:
                    obj[neto.tag] = neto.text
                data.append(obj)
            if(tipo == 'simples'):
                return SimpleReport.generate(data)
            else:
                return CompleteReport.generate(data)
