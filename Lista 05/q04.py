vetor = []

a = 1
b= 1
c = 0
vetor.append(a)
vetor.append(b)

for i in range(1,19):
    c = a + b
    vetor.append(c)
    a = b
    b = c

print(vetor)
