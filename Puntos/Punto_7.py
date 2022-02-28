import numpy as np


def punto_7(x):
    matriz = np.zeros((x, x))

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:
                matriz[i][j] = i + 1
            elif i < j:
                matriz[i][j] = 2 * (i + 1) + 5 * (j + 1)
            else:
                matriz[i][j] = 3 * (i + 1) + 4 * (j + 1)
    for r in matriz:
        print(r)


if __name__ == '__main__':
    try:
        orden = int(input("Ingrese el orden de matriz deseado: "))
    except (ValueError, SyntaxError):
        print("Error: El numero ingresado deve ser entero positivo")
    else:
        punto_7(orden)
