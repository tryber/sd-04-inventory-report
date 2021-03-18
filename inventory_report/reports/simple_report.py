from datetime import datetime
from functools import reduce


def transform_string_to_date(string_param):
    return datetime.strptime(string_param, "%Y-%m-%d")


class SimpleReport:
    @classmethod
    def generate(cls, dataReport):
        def get_oldest_fab_date(products_list):
            products_list.sort(
                key=lambda product: transform_string_to_date(
                    product["data_de_fabricacao"]
                )
            )
            return products_list[0]["data_de_fabricacao"]

        def get_closest_validity(products_list):
            today = datetime.today()
            next_validity_dates = [
                product["data_de_validade"]
                for product in products_list
                if today
                < transform_string_to_date(product["data_de_validade"])
            ]
            return min(next_validity_dates)

        def get_company_with_more_products(products_list):
            companies_dict = {}
            for product in products_list:
                company_name = product["nome_da_empresa"]
                if hasattr(companies_dict, company_name):
                    companies_dict[company_name] += 1
                else:
                    companies_dict[company_name] = 1
            return reduce(lambda a, b: a if a > b else b, companies_dict)

        oldest_fab_date = get_oldest_fab_date(dataReport)
        closest_validity = get_closest_validity(dataReport)
        company = get_company_with_more_products(dataReport)

        return f"""Data de fabricação mais antiga: {oldest_fab_date}
Data de validade mais próxima: {closest_validity}
Empresa com maior quantidade de produtos estocados: {company}
"""
