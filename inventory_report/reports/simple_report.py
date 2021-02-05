from datetime import datetime
import collections

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
            [stock["data_de_fabricacao"] for stock in data]
        )

        validade_mais_proxima = min(
            [
                stock["data_de_validade"]
                for stock in data
                if datetime.now()
                < datetime.strptime(stock["data_de_validade"], "%Y-%m-%d")
            ]
        )

        estoque = max(
            collections.Counter([stock["nome_da_empresa"] for stock in data])
        )

        return (
            f"Data de fabricação mais antiga: {fabricacao_mais_antiga}\n"
            f"Data de validade mais próxima: {validade_mais_proxima}\n"
            f"Empresa com maior quantidade de produtos estocados: {estoque}\n"
        )
