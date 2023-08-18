def exponencial(base, exp):
    if exp == 0:
        return 1
    
    else:
        return base * exponencial(base, exp-1)


print(exponencial(2, 0))
print(exponencial(2, 4))
print(exponencial(2, 9))