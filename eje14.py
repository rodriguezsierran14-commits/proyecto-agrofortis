inicio = int(input("Ingresa el número donde quieres comenzar: "))
limite = int(input("Ingresa el número límite: "))

i = inicio

while i <= limite:
    print("\nTabla del", i)

    multiplicador = 1

    while multiplicador <= 10:
        resultado = i * multiplicador
        print(i, "x", multiplicador, "=", resultado)
        multiplicador = multiplicador + 1

    i = i + 1