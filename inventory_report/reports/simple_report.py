import datetime


class SimpleReport:
    @classmethod
    def generate(cls, dict_list):
        today = f"{datetime.date.today()}"

        oldest_fabricated_date = min(
            [x["data_de_fabricacao"] for x in dict_list]
        )

        next_expired_date = min(
            [
                x["data_de_validade"]
                for x in dict_list
                if x["data_de_validade"] > today
            ]
        )
        all_company_name_list = [x["nome_da_empresa"] for x in dict_list]
        most_stocked_company = max(
            set(all_company_name_list), key=all_company_name_list.count
        )
        report_ofd = "Data de fabricação mais antiga: "
        report_ned = "Data de validade mais próxima: "
        report_msc = "Empresa com maior quantidade de produtos estocados: "
        return (
            f"{report_ofd}{oldest_fabricated_date}\n"
            f"{report_ned}{next_expired_date}\n"
            f"{report_msc}{most_stocked_company}\n"
        )
