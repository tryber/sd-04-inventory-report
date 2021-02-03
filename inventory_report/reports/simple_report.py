from datetime import datetime
import collections

mock = [
    {
        "id": 1,
        "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2020-07-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
        "instrucoes_de_armazenamento": "in blandit ultrices enim",
    },
    {
        "id": 2,
        "nome_do_produto": "sodium ferric gluconate complex",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2020-05-31",
        "data_de_validade": "2023-01-17",
        "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
        "instrucoes_de_armazenamento": "duis bibendum morbi",
    },
    {
        "id": 3,
        "nome_do_produto": "Dexamethasone Sodium Phosphate",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2019-09-13",
        "data_de_validade": "2023-02-13",
        "numero_de_serie": "BA52 2034 8595 7904 7131",
        "instrucoes_de_armazenamento": "morbi quis tortor id",
    },
    {
        "id": 4,
        "nome_do_produto": "Uricum acidum, Benzoicum acidum",
        "nome_da_empresa": "Newton Laboratories",
        "data_de_fabricacao": "2019-11-08",
        "data_de_validade": "2019-11-25",
        "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
        "instrucoes_de_armazenamento": "velit eu est congue elementum",
    },
]

# Para criar métodos de classe em Python, precisamos de adicionar um
# @classmethod em sua assinatura.

# Observe também que em métodos de classe o parâmetro self é substituído
# pelo cls. Isto indica que receberemos uma classe e não uma instância,
# o que pode ser particularmente útil caso seja necessário acessar alguma
# informação da classe, como por exemplo, uma constante.


class SimpleReport:
    # Class method 'generate' should have 'cls' as first argument.
    @classmethod
    def generate(cls, data):
        fabricacao_mais_antiga = min(
            [stock["data_de_fabricacao"] for stock in mock]
        )

        validade_mais_proxima = min(
            [
                stock["data_de_validade"]
                for stock in mock
                if datetime.now()
                < datetime.strptime(stock["data_de_validade"], "%Y-%m-%d")
            ]
        )

        estoque = max(
            collections.Counter([stock["nome_da_empresa"] for stock in mock])
        )

        return (
            f"Data de fabricação mais antiga: {fabricacao_mais_antiga}\n"
            f"Data de validade mais próxima: {validade_mais_proxima}\n"
            f"Empresa com maior quantidade de produtos estocados: {estoque}\n"
        )
