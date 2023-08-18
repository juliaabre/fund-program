from random import randint

vetor = []

for v in range(0, 10):
    n = randint(0, 100)
    if n in vetor:
        print(f'O número {n} já está na {vetor.index(n)+1}ª posição')
        continue
    else:
        vetor.append(n)

print(vetor)
