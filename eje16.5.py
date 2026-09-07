estrato = int(input("Ingrese el estrato del estudiante: "))
edad = int(input("Ingrese la edad del estudiante: "))
matricula = float(input("Ingrese el valor de la matrícula: "))

if estrato == 1:
    if edad < 18:
        descuento = 0.20
    else:
        descuento = 0.15

elif estrato == 2:
    if edad < 18:
        descuento = 0.10
    else:
        descuento = 0.05

else:
    descuento = 0

valor_descuento = matricula * descuento
valor_pagar = matricula - valor_descuento

print("Valor de la matrícula:", matricula)
print("Valor del descuento:", valor_descuento)
print("Valor que debe pagar:", valor_pagar)