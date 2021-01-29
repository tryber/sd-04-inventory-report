from datetime import date
from collections import Counter


class simpleReport:
    def generate(self, data):
        today = date.today

        dataFabr = min(
            [simpleData["data_de_fabricacao"] for simpleData in data]
        )
        dataValid = min(
            [
                simpleData["data_de_validade"]
                for simpleData in data
                if simpleData["data_de_validade"] > today
            ]
        )
        Emp = max(
            Counter(simpleData["nome_da_empresa"] for simpleData in data)
        )

        stringDeRetorno = (
            f"Data de fabricação mais antiga: {dataFabr}\n"
            + f"Data de validade mais próxima: {dataValid}\n"
            + f"Empresa com maior quantidade de produtos estocados: {Emp}\n"
        )

        return stringDeRetorno


# for simpleDataFab in data:
# if(data.data_de_fabricacao <= dataFabr):
# dataFabr = data.data_de_fabricacao
# return dataFabr
# else :
# return dataFabr

# for simpleDataValid in data:
# if(data.data_de_validade >= dataValid and data.data_de_validade <= today ):
# dataValid = data.data_de_validade
# return dataValid
# else :
# return dataValid
