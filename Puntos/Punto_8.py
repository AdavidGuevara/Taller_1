from Punto_5y6 import punto_5

# epsilon = np.finfo(float).eps
epsilon = punto_5()
numero_inicial = 5
contador = 0

while numero_inicial < 5.001:
    numero_inicial += epsilon
    contador += 1
    print(contador)

print(f"El total de numeros que estan entre 5 y 5.001: {contador}")
