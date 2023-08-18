def CalculaIMC(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def ClassificaIMC(imc):
    if imc < 18.5:
        resultado = 'magreza'
    elif 18.5 <= imc < 24.9:
        resultado = 'normal'
    elif 25 <= imc < 29.9:
        resultado = 'sobrepeso com grau de obesidade 1'
    elif 30 <= imc < 39.9:
        resultado = 'obesidade com grau de obesidade 2'
    elif imc >= 40:
        resultado = 'obesidade grave com grau de obesidade 3'
    return resultado

peso = float(input('Informe o peso: '))
altura = float(input('Informe a altura: '))
print(f'O valor do IMC é {CalculaIMC(peso,altura):.1f} e tem como classificação {ClassificaIMC(CalculaIMC(peso,altura))}')
