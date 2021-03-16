from datetime import date
from collections import defaultdict
from functools import reduce


class SimpleReport:
    def generate(dict_list):
        today = date.today()
        olddest_date = None
        closest_validity = None
        company_count = defaultdict(lambda: 0)

        def get_date(report, key, old_value, min_date=False):
            year, month, day = report[key].split("-")
            date_report = date(year=int(year), month=int(month), day=int(day))
            if min_date and date_report < today:
                return old_value
            if old_value is None or date_report < old_value:
                return date_report
            return old_value

        for report in dict_list:
            olddest_date = get_date(report, "data_de_fabricacao", olddest_date)

            closest_validity = get_date(
                report, "data_de_validade", closest_validity, True
            )

            company_count[report["nome_da_empresa"]] += 1

        company = reduce(lambda a, b: a if a > b else b, company_count)

        return f"""Data de fabricação mais antiga: {olddest_date}
Data de validade mais próxima: {closest_validity}
Empresa com maior quantidade de produtos estocados: {company}
"""
