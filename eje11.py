import math

entrada = input('Ingresa el radio del círculo: ')

if entrada.replace('.', '1').isdigit():
    radio = float(entrada)

    if radio >= 0:
        area = math.pi * radio ** 2
        print(f'El área del círculo es: {area:.2f}')
    else:
        print('Error: el radio no puede ser negativo.')
else:
    print('Error: debes ingresar un número válido.')