inicio = int(input("Ingresa el número donde quieres comenzar: "))
limite = int(input("Ingresa el número límite: "))

i = inicio
paso = 1

print("\nPaso | i | multiplicador | resultado | Condición")

while i <= limite:

    multiplicador = 1

    print(paso, "|", i, "| - | - |", i, "<=", limite, "-> Verdadero")
    paso = paso + 1

    while multiplicador <= 10:

        resultado = i * multiplicador

        print(paso, "|", i, "|", multiplicador, "|", resultado,
              "|", multiplicador, "<= 10 -> Verdadero")

        multiplicador = multiplicador + 1
        paso = paso + 1

    print(paso, "|", i, "|", multiplicador, "| - |",
          multiplicador, "<= 10 -> Falso")

    paso = paso + 1
    i = i + 1

print(paso, "|", i, "| - | - |", i, "<=", limite, "-> Falso -> FIN")