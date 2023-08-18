funcionarios = [[], [], [], []]
maior = menor = 0

for i in range(0, 4):
    matricula = int(input('Informe a matrícula do funcionário: '))
    funcionarios[i].append(matricula)

    nome = input('Informe o nome do funcionário: ')
    funcionarios[i].append(nome)

    funcao = input('Informe a função do funcionário: ')
    funcionarios[i].append(funcao)

    salario = int(input('Informe o salário do funcionário: '))
    funcionarios[i].append(salario)
    if i == 0:
        maior = menor = salario
    elif salario > maior:
        maior = salario
    elif salario < menor:
        menor = salario
    print(" ")

for i in range(0, 4):
    for l in range(0, 4):
        print(f'{funcionarios[i][l]:^15}', end=" ")
    print('\n')

print(f'O maior salário tem o valor de R${maior} e o menor salário é de R${menor}.')
