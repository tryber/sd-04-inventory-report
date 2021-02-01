from inventory_report.importer.importer import Importer


class CSVImporter(Importer):
    @classmethod
    def import_data(cls, pathname):
        return super().import_data(pathname)