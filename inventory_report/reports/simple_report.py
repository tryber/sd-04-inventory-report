from datetime import datetime


class SimpleReport:
    def generate(data):
        datas_fabricacao = []
        datas_validade = []
        empresas = []

        for product in data:
            datas_fabricacao.append(
                datetime.strptime(product["data_de_fabricacao"], "%Y-%m-%d")
            )
            datas_validade.append(
                datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
            )
            empresas.append(product["nome_da_empresa"])

        data_mais_antiga = min(datas_fabricacao).date()
        data_mais_proxima = min(
            validade
            for validade in datas_validade
            if validade > datetime.now()
        ).date()
        empresa = max(set(empresas), key=empresas.count)

        return (
            f"Data de fabricação mais antiga: {data_mais_antiga}\n"
            f"Data de validade mais próxima: {data_mais_proxima}\n"
            f"Empresa com maior quantidade de produtos estocados: {empresa}\n"
        )
