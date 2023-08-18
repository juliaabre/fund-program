from random import randint

vetor = []
primos = []

def Primo(n):
    mult = 0
    for c in range(2, n):
        if n % c == 0:
            mult += 1

    if mult == 0:
       return primos.append(n)

for i in range(1, 11):
    n = randint(0, 100)
    if n in vetor:
        continue
    else:
        vetor.append(n)  
    Primo(n)          

print(f'Lista dos Números: {vetor}')
print(f'Lista dos Números Primos: {primos}')
print(f'Quantidade de Números Primos: {len(primos)}')


