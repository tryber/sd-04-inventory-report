import collections


example_list = [
  {
    "id": 1,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2020-07-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  },
  {
    "id": 2,
    "nome_do_produto": "DETERGENTE LIQUIDO",
    "nome_da_empresa": "EMPRESA FAKE",
    "data_de_fabricacao": "2019-05-09",
    "data_de_validade": "2024-05-10",
    "numero_de_serie": "FR40 2002 7680 97V4 W6FO LEBO 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  },
  {
    "id": 3,
    "nome_do_produto": "DETERGENTE LIQUIDO",
    "nome_da_empresa": "EMPRESA FAKE",
    "data_de_fabricacao": "2019-05-02",
    "data_de_validade": "2024-05-11",
    "numero_de_serie": "FR40 2002 7680 97V4 W6FO LEBO 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  }
]

data_de_hoje = "2023-05-09"

oldest_fabricated_date = min([x['data_de_fabricacao'] for x in example_list])

next_expire_date = min([x['data_de_validade'] for x in example_list if x["data_de_validade"] > data_de_hoje])
most_stocked_company = [x['nome_da_empresa'] for x in example_list]

company = (max(set(most_stocked_company), key=most_stocked_company.count))
# print(collections.Counter(most_stocked_company))
[x['data_de_fabricacao'] for x in example_list]
print(oldest_fabricated_date)
print(next_expire_date)
print(most_stocked_company)

print(f"Data de fabricação mais antiga: {oldest_fabricated_date}\nData de validade mais próxima: {next_expire_date}\nEmpresa com maior quantidade de produtos estocados: {company}")
