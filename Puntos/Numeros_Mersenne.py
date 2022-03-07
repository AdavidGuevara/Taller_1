import time
import math


def evaluar_primo(numero):
    primo = False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            primo = True
            break
    return primo


def numeros_mersenne(rango):
    mersenne_lista = []
    contador = 0
    for i in range(2, rango):
        if not evaluar_primo(i):
            mersenne = (2**i)-1
            mersenne_lista.append(mersenne)
            contador += 1
    return mersenne_lista, contador


if __name__ == '__main__':
    try:
        maximo = int(input("Ingrese el maximo del intervalo deseado: "))
    except (ValueError, SyntaxError):
        print("Error: El numero ingresado deve ser entero positivo")
    else:
        fin_1 = time.time()
        vector, total = numeros_mersenne(maximo)
        print(" ")
        print(vector)
        fin_2 = time.time()
        print(f"Total de numeros de mersenne en el intervalo [0, {maximo}]: {total}")
        print(f"Tiempo de ejecucion del programa: {fin_2 - fin_1}")
