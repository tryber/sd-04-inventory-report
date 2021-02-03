from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(data):        

        company_name = []
        for product in data:
            company_name.append(product['nome_da_empresa'])
        
        company_name_qtd = Counter(company_name).items()
        message = []
    
        for k, v in dict(company_name_qtd).items():
            message.append(f"- {k}: {v}")
        
        format_message = '\n'.join(message)
       
        complete_report = (
            f"{SimpleReport.generate(data)}\n"
            f"Produtos estocados por empresa: \n"
            f"{format_message}\n"
        )
        return complete_report
