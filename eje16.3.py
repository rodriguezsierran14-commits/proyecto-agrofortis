temperatura = float(input("Ingrese la temperatura de la máquina: "))

motor = "encendido"

print("El motor está encendido.")

if temperatura > 80:
    motor = "apagado"
    print("La temperatura supera los 80 grados.")
    print("El motor se apagó automáticamente.")
else:
    print("La temperatura es segura.")
    print("El motor continúa encendido.")

print("Estado final del motor:", motor)