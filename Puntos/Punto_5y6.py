

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

# Si epsilon satisface la condicion: (epsilon < x) para todos los numeros x que la maquina soporta, entonces
# (1/x < 1/epsilon) para todos los reales x que la maquina soporta.
