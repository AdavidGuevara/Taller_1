promedios = [58, 61, 89, 45, 75, 92, 85, 23, 35, 87, 71, 66]
inasistencias = [40, 50, 65, 70, 10, 22, 15, 3, 10, 8, 1, 6]

contador = 0

for i in range(len(promedios)):
    if promedios[i] > 60 and inasistencias[i] < 40:
        contador += 1

print(f"El numero total de estudiantes que aprivaron es: {contador}")
