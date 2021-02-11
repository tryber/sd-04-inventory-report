from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, lista):
        string_return = cls.produtos_por_empresa(lista.copy())
        return (
            f"Data de fabricação mais antiga: {cls.get_antiga(lista.copy())}\n"
            f"Data de validade mais próxima: {cls.get_proxima(lista.copy())}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{cls.get_empresa(lista.copy())}\n\n"
            "Produtos estocados por empresa: \n"
            f"{string_return}"
        )

    def produtos_por_empresa(lista):
        counter = {}
        for dic in lista:
            key = dic["nome_da_empresa"]
            counter[key] = counter.get(key, 0) + 1
        return_string = ""
        for key, value in counter.items():
            return_string += f"- {key}: {str(value)}\n"
        return return_string
