def punto_2():
    multiplos = []
    try:
        numero = int(input("Ingrese el numero a calcular sus multiplos: "))
    except (ValueError, SyntaxError):
        print("El numero ingresado deve ser un entero")
    else:
        contador = numero
        while contador != 0:
            if numero % contador == 0:
                multiplos.append(contador)
            contador -= 1
        print(multiplos)


if __name__ == '__main__':
    punto_2()
