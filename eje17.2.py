suma = 0
pares = 0
impares = 0
cantidad = 0

numero = int(input("Ingrese un número (negativo para terminar): "))

while numero >= 0:
    suma += numero
    cantidad += 1

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if cantidad == 1:
        menor = numero
        mayor = numero
    else:
        if numero < menor:
            menor = numero

        if numero > mayor:
            mayor = numero

    numero = int(input("Ingrese otro número (negativo para terminar): "))

print("\n--- RESULTADOS ---")
print("Sumatoria:", suma)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)

if cantidad > 0:
    print("Número menor:", menor)
    print("Número mayor:", mayor)
else:
    print("No se ingresaron números.")