matriz = [[], [], [], [], [], [], [], [], [], [], [], []]
lista_colocacao = []
lista_copa_americana = []
lista_rebaixados = []

for i in range(0, 12):
    nome = input('Informe o nome do time: ')
    matriz[i].append(nome)

    posicao = int(input('Informe a posição do time: '))
    matriz[i].append(posicao)
    if posicao <= 5:
        lista_colocacao.append(nome)
    elif 6 <= posicao <= 10:
        lista_copa_americana.append(nome)
    elif posicao > 10:
        lista_rebaixados.append(nome)

    pontos = int(input('Informe a quantidade de pontos: '))
    matriz[i].append(pontos)

    jogos = int(input('Informe a quantidade de jogos: '))
    matriz[i].append(jogos)

    vitorias = int(input('Informe a quantidade de vitórias: '))
    matriz[i].append(vitorias)

    empates = int(input('Informe o número de empates: '))
    matriz[i].append(empates)

    derrotas = int(input('Informe o número de derrotas: '))
    matriz[i].append(derrotas)
    print()


for l in range(0, 12):
    for c in range(0, 7):
        print(f'{matriz[l][c]:^15}', end='')
    print()

print(f'O campeao é {lista_colocacao[0]}')
print(f'Os classificados para a Libertadores da America são {lista_colocacao}')
print(f'Os classificados para a Copa sul-americana são {lista_copa_americana}')
print(f'Os times rebaixados são {lista_rebaixados}')
    