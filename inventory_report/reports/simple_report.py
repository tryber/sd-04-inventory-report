from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, lista):

        return f"""Data de fabricação mais antiga: \\
{cls.get_fabricacao_mais_antiga(lista)}
Data de validade mais próxima: \\
{cls.get_validade_mais_proxima(lista)}
Empresa com maior quantidade de produtos estocados: \\
{cls.get_empresa_com_mais_produtos(lista)}
        """

    def get_fabricacao_mais_antiga(lista):
        lista.sort(
            key=lambda item: datetime.strptime(
                item["data_de_fabricacao"], "%Y-%m-%d"
            )
        )
        return lista[0]["data_de_fabricacao"]

    def get_validade_mais_proxima(lista):
        lista.sort(
            key=lambda item: datetime.strptime(
                item["data_de_validade"], "%Y-%m-%d"
            )
        )
        return lista[0]["data_de_validade"]

    def get_empresa_com_mais_produtos(lista):

        counter = {}

        for dic in lista:
            key = dic["nome_da_empresa"]
            counter[key] = counter.get(key, 0) + 1

        return sorted(counter.items(), key=lambda kv: kv[1])[-1][0]
