import time


def encontrar_primo_1(numero):
    contador_multiplo = 0
    for i in range(2, int(numero/2) + 1):
        if numero % i == 0:
            contador_multiplo += 1
            break
    if contador_multiplo > 0:
        return True
    else:
        return False


def primo_1(rango):
    primos = []
    contador = 0
    for i in range(2, rango):
        if not encontrar_primo_1(i):
            primos.append(i)
            contador += 1
    return primos, contador


if __name__ == '__main__':
    try:
        maximo = int(input("Ingrese el maximo del intervalo deseado: "))
    except (ValueError, SyntaxError):
        print("Error: El numero ingresado deve ser entero positivo")
    else:

        inicio_1 = time.time()
        vector_1, total_1 = primo_1(maximo)
        print(vector_1)
        print(total_1)
        fin_1 = time.time()
        print(f"Tiempo de ejecucion al dividir numero a la mitad: {fin_1-inicio_1}")
