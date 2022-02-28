

def punto_5():
    numeros = []
    epsilon = 1

    while epsilon > 0:
        epsilon = epsilon / 2
        numeros.append(epsilon)
    return numeros


if __name__ == '__main__':
    solucion = punto_5()
    numero = len(solucion)
    print(f"El numero mas pequeño es: {solucion[numero-2]}")
    print(f"El numero mas grande es: {1/solucion[numero-53]}, tomando el numero {solucion[numero-53]}")
