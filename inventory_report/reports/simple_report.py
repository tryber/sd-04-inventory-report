from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, lista):

        return (
            f"Data de fabricação mais antiga: {cls.get_antiga(lista)}\n"
            f"Data de validade mais próxima: {cls.get_proxima(lista)}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{cls.get_empresa(lista)}"
        )

    def get_antiga(lista):
        lista.sort(
            key=lambda item: datetime.strptime(
                item["data_de_fabricacao"], "%Y-%m-%d"
            )
        )
        return lista[0]["data_de_fabricacao"]

    def get_proxima(lista):
        today = datetime.today()

        filtered_lista = list(
            (
                filter(
                    lambda item: datetime.strptime(
                        item["data_de_validade"], "%Y-%m-%d"
                    )
                    > today,
                    lista,
                )
            )
        )

        sorted_lista = sorted(
            filtered_lista,
            key=lambda item: datetime.strptime(
                item["data_de_validade"], "%Y-%m-%d"
            ),
        )

        return sorted_lista[0]["data_de_validade"]

    def get_empresa(lista):

        counter = {}

        for dic in lista:
            key = dic["nome_da_empresa"]
            counter[key] = counter.get(key, 0) + 1

        return sorted(counter.items(), key=lambda kv: kv[1])[-1][0]
