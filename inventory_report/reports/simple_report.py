import datetime


class SimpleReport:
    def __init__(self, data_list):
        self.data_de_hoje = f"{datetime.date.today()}" 
        self.oldest_fabricated_date = min([x['data_de_fabricacao'] for x in data_list])
        self.next_expired_date = min([x['data_de_validade'] for x in data_list if x["data_de_validade"] > self.data_de_hoje])
        self.most_stocked_company = [x['nome_da_empresa'] for x in data_list]
        self.bigger_stock_company = (max(set(self.most_stocked_company), key=self.most_stocked_company.count))

    def generate(self):
        return (f"Data de fabricação mais antiga: {self.oldest_fabricated_date}\nData de validade mais próxima: {self.next_expired_date}\nEmpresa com maior quantidade de produtos estocados: {self.bigger_stock_company}")


report = SimpleReport([
  {
    "id": 1,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2020-07-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  }
])

print(f"{report.generate()}")
