from datetime import datetime
from collections import Counter

dataReport = [
    {
          "id": 1,
          "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
          "nome_da_empresa": "Forces of Nature",
          "data_de_fabricacao": "2020-07-04",
          "data_de_validade": "2023-02-09",
          "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
          "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus",
    }
]


class SimpleReport():
    @classmethod
    def generate(self, dataReport):
        report = {}
        report["max_date"] = 
        report["max_validate_date"] = 
        report["max_quantity"] = max(Counter(dataReport).most_common)

        print(f"""Data de fabricação mais antiga: {report["max_date"]}\n
        Data de validade mais próxima: {report["max_validate_date"]}\n
        Empresa com maior quantidade de produtos estocados: {report["max_quantity"]}\n""")

    def getOldFabDate():    
        
        return oldest_fabric_date

    def getNextValidateDate():  
        return next_validate_date
    def getMaxQuantity():    
        return bigger_quantity
# - O método deverá retornar uma saída com o seguinte formato:

#    ```bash
#    Data de fabricação mais antiga: YYYY-MM-DD
#    Data de validade mais próxima: YYYY-MM-DD
#    Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA
#    ```
# - A data de validade mais próxima, somente considera itens que ainda não venceram.