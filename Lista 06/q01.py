cliente = [[], [], [], [], []]

for i in range(0, 5):
    nome = input('Informe o nome do cliente: ')
    cliente[i].append(nome)

    numConta = int(input('Informe o número da conta: '))
    cliente[i].append(numConta)

    saldo = float(input('Informe o saldo da conta: '))
    cliente[i].append(saldo)

    op = input('Informe a Operação: ')
    cliente[i].append(op)
    print(' ')

for i in range(0, 5):
    for l in range(0, 4):
        print(f'{cliente[i][l]:^15}', end="")
    print('\n')
