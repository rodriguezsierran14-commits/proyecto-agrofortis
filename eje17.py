inicio = int(input("Ingrese el número inicial: "))
fin = int(input("Ingrese el número final: "))

for numero in range(inicio, fin + 1, 2):
    print(numero)
    inicio = int(input("Ingrese el número inicial: "))
fin = int(input("Ingrese el número final: "))

for numero in range(inicio, fin + 1, 2):
    print(numero)

for numero in range(fin - 2, inicio - 1, -2):
    print(numero)