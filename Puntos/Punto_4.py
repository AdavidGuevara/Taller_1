promedios = [58, 61, 89, 45, 75, 92, 85, 23, 35, 87, 71, 66]
inasistencias = [40, 50, 65, 70, 10, 22, 15, 3, 10, 8, 1, 6]

contador = 0

promedio = float(input("Ingrese el porcentaje del promedio de aprovacion: "))
inasistencia = float(input("Ingrese el porcentaje maximo de de inasistencia permitida: "))

for i in range(len(promedios)):
    if promedios[i] > promedio and inasistencias[i] < inasistencia:
        contador += 1

print(f"El numero total de estudiantes que aprovaron es: {contador}")
