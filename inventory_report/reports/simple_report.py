import datetime


class SimpleReport:
    def __init__(self, dict_list):
        self.data_de_hoje = f"{datetime.date.today()}"

        self.oldest_fabricated_date = min(
            [x["data_de_fabricacao"] for x in dict_list]
        )

        self.next_expired_date = min(
            [
                x["data_de_validade"]
                for x in dict_list
                if x["data_de_validade"] > self.data_de_hoje
            ]
        )
        self.most_stocked_company = [x["nome_da_empresa"] for x in dict_list]
        self.bigger_stock_company = max(
            set(self.most_stocked_company), key=self.most_stocked_company.count
        )

    def generate(self):
        return (
            f"""Data de fabricação mais antiga: {self.oldest_fabricated_date}\n
            Data de validade mais próxima: {self.next_expired_date}\n
            Empresa com maior quantidade de produtos estocados:
            {self.bigger_stock_company}"""
        )
