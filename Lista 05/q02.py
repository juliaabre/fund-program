vetor1 = []
vetor2 = []
soma1 = 0
soma2 = 0
# Quadrado dos números pares
for i in range(1, 21):
    if i % 2 == 0:
        n = i ** 2
        vetor1.append(n)
    else:
        continue
# Segundo valor
for i in range(10, 20):
    vetor2.append(i)
#Soma dos Vetores
for n in vetor1:
    soma1 += n
for m in vetor2:
    soma2 += m
soma = soma1 + soma2
print(f'O primeiro vetor: {vetor1}')
print(f'O segundo vetor: {vetor2}')
print(f'A soma dos dois vetores é: {soma}')
