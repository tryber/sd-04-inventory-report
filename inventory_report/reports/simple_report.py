from datetime import datetime


class SimpleReport:
    def __init__(self, report):
        self.report = report

    @classmethod
    def generate(cls, report):
        def get_min_date(dates_list):
            datetimes_list = [
                datetime.strptime(date, "%Y-%m-%d") for date in dates_list
            ]
            get_min = min(datetimes_list)
            return get_min.strftime("%Y-%m-%d")

        def count_occurrence(list):
            count_items = {i: list.count(i) for i in list}
            return count_items

        def oldest_manufacturing_date():
            fabrication_list = [x["data_de_fabricacao"] for x in report]
            return get_min_date(fabrication_list)

        def closest_expiration_date():
            today = datetime.strftime(datetime.now(), "%Y-%m-%d")
            expiration_date_list = [
                x["data_de_validade"]
                for x in report
                if x["data_de_validade"] > today
            ]
            return get_min_date(expiration_date_list)

        def max_company_occurrence():
            companies_list = [x["nome_da_empresa"] for x in report]
            print("companies_list:", companies_list)
            # count_companies = {
            #     i: companies_list.count(i) for i in companies_list
            # }
            count_companies = count_occurrence(companies_list)
            print("count_companies:", count_companies)
            max_company_value = max(count_companies, key=count_companies.get)
            return max_company_value

        manufacturing = oldest_manufacturing_date()
        expiration = closest_expiration_date()
        company = max_company_occurrence()

        return (
            f"Data de fabricação mais antiga: {manufacturing}\n"
            f"Data de validade mais próxima: {expiration}\n"
            f"Empresa com maior quantidade de produtos estocados: {company}\n"
        )
