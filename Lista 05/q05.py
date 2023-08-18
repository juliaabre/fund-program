vetor = []
pares = []

for v in range(10, 21):
    vetor.append(v)
    if v % 2 == 0:
        pares.append(v)

print(sorted(pares, reverse=True))