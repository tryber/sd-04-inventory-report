from datetime import date
from collections import defaultdict
from functools import reduce


class SimpleReport:
    def generate(new_list):
        today = date.today()
        oldest = None
        ending = None
        entreprise_count = defaultdict(lambda: 0)

        def get_date(report, key, old_value, min_date=False):
            year, month, day = report[key].split("-")
            date_report = date(year=int(year), month=int(month), day=int(day))
            if min_date and date_report < today:
                return old_value
            if old_value is None or date_report < old_value:
                return date_report
            return old_value

        for report in new_list:
            oldest = get_date(report, "data_de_fabricacao", oldest)

            ending = get_date(
                report, "data_de_validade", ending, True
            )

            entreprise_count[report["nome_da_empresa"]] += 1

        company = reduce(lambda a, b: a if a > b else b, entreprise_count)

        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {ending}\n"
            f"Empresa com maior quantidade de produtos estocados: {company}\n"
        )
