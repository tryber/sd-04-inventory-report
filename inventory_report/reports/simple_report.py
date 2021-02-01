import datetime
import collections


class SimpleReport:
    def generate(data):
        fabricationDate = []
        validityDate = []
        company = []

        for x in data:
            fabricationDate.append(
                datetime.datetime.strptime(x["data_de_fabricacao"], "%Y-%m-%d")
            )
            validityDate.append(
                datetime.datetime.strptime(x["data_de_validade"], "%Y-%m-%d")
            )
            company.append(x["nome_da_empresa"])

        oldestDate = min(fabricationDate).date()
        nearestDate = min(
            validity for validity in validityDate
            if validity > datetime.datetime.now()
        ).date()
        company = collections.Counter(company).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldestDate}\n"
            f"Data de validade mais próxima: {nearestDate}\n"
            f"Empresa com maior quantidade de produtos estocados: {company}\n"
        )
