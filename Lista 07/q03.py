def Saque(valor):
        
    cedula_200 = cedula_100 = cedula_50 = cedula_20 = cedula_10 = cedula_5 = cedula_2 = 0

    while valor != 0:

        if valor % 200 == 0:
            cedula_200 += 1
            valor -= 200
            continue

        if valor % 100 == 0:
            cedula_100 += 1
            valor -= 100
            continue

        if valor % 50 == 0:
            cedula_50 += 1
            valor -= 50
            continue

        if valor % 20 == 0:
            cedula_20 += 1
            valor -= 20
            continue

        if valor % 10 == 0:
            cedula_10 += 1
            valor -= 10
            continue

        if valor % 5 == 0:
            cedula_5 += 1
            valor -= 5
            continue
        
        if valor % 2 == 0:
            cedula_2 += 1
            valor -= 2
            continue


        if valor < 4:
            print("Operação inválida.")
            break

        if valor % valor == 0 and valor % 1 == 0:
            if valor > 5:
                cedula_5 += 1
                valor = valor - 5
            if valor > 2:
                cedula_2 += 1
                valor = valor - 2


    print(f'{cedula_200} de 200')
    print(f'{cedula_100} de 100')
    print(f'{cedula_50} de 50')
    print(f'{cedula_20} de 20')
    print(f'{cedula_10} de 10')
    print(f'{cedula_5} de 5')
    print(f'{cedula_2} de 2')
    print()
        

Saque(6)
Saque(8)
Saque(11)
Saque(13)
Saque(4)
Saque(3)
