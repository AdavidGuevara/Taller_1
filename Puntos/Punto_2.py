def punto_2():
    multiplos = []
    try:
        numero = int(input("Ingrese el numero a calcular sus multiplos: "))
        contador = int(input("Ingrese el numero maximo del intervalo: "))
    except (ValueError, SyntaxError):
        print("El numero ingresado deve ser un entero")
    else:
        while contador != 0:
            if contador % numero == 0:
                multiplos.append(contador)
            contador -= 1
        print(multiplos)


if __name__ == '__main__':
    punto_2()
