from random import randint

vetor = []

while len(vetor) < 10:
    n = randint(0, 100)
    if n in vetor:
      continue
    else:
         vetor.append(n)

print(f'Lista Crescente: {sorted(vetor)}')
print(f'Lista Decrescente: {sorted(vetor, reverse=True)}')