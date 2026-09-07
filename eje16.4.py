conexion = float(input("Ingrese la velocidad de conexión en Mbps: "))

if conexion > 20:
    descarga = 10
elif conexion > 5:
    descarga = 5
else:
    descarga = 1

print("La velocidad de descarga será de:", descarga, "Mbps")