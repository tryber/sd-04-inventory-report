import json
from collections import Counter

with open('../data/inventory.json', 'r') as file:
    content = file.read()
    data = json.loads(content)
 

company_name = []

for test in data:    
    company_name.append(test['nome_da_empresa'])

print(company_name)
company_great_than_qtd = Counter(company_name)
print(company_great_than_qtd)

class SimpleReport:
    def __init__(self, stock):
        self.stock = stock

    def generate(self):
        # Leitura do arquivo
        with open(self.stock) as file:
            result = json.load(file)
        print(result)

        # compara a chave data_de_fabricacao de todos os objetos para encontrar a mais antiga
        print("Data de fabricação mais antiga: YYYY-MM-DD")

        # compara a chave data_de_validade de todos os objetos para encontrar a mais próxima, que ainda não venceu
        print("Data de validade mais próxima: YYYY-MM-DD")

        # Utilizar a chave nome_da_empresa para contar a quantidade de produtos da empresa
        # Depois comparar esses valores para ver quem tem o maior número de produtos estocados.
        print("Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA")
