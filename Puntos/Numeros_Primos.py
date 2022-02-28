

def encontrar_primo(numero):
    contador_multiplo = 0
    for i in range(2, int(numero/2) + 1):
        if numero % i == 0:
            contador_multiplo += 1
            break
    if contador_multiplo > 0:
        return True
    else:
        return False


def primo(rango):
    primos = []
    contador = 0
    for i in range(2, rango):
        if not encontrar_primo(i):
            primos.append(i)
            contador += 1
    return primos, contador


if __name__ == '__main__':
    try:
        maximo = int(input("Ingrese el maximo del intervalo deseado: "))
    except (ValueError, SyntaxError):
        print("Error: El numero ingresado deve ser entero positivo")
    else:
        vector, total = primo(maximo)
        print(vector)
        print(total)
