data = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o dia: '))

data_atual = int(input('Informe o dia atual: '))
mes_atual = int(input('Informe o mes atual: '))
ano_atual = int(input('Digite o ano atual: '))

def CalculaDias(data, mes, ano):
    anos = ano_atual - ano
    if mes_atual == mes:
        idade_anos = ano_atual - ano
        idade_mes = 0
    elif mes_atual < mes:
        idade_anos = anos - 1
        idade_mes = (mes_atual - mes) + 12
    elif mes_atual > mes:
        idade_anos = anos
        idade_mes = mes_atual - mes
    idade_mes *= 30
    idade_anos *= 365
    dias = idade_mes + idade_anos
    return dias

print(CalculaDias(data, mes, ano))
