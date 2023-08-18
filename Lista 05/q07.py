from random import randint

vetor = []
pares = 0
impares = 0

for v in range(0, 10):
    n = randint(0, 100)
    if n in vetor:
        continue
    else:
        vetor.append(n)
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1

print(vetor)
print(f'Existe na lista {pares} números pares.')
print(f'Existe na lista {impares} números impares.')
