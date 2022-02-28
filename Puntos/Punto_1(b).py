def multiplos_2():
    multiplos = []
    try:
        denominador = int(input("Ingrese el numero que sera el multiplo: "))
    except (ValueError, SyntaxError):
        print("El numero ingresado deve ser un entero positivo")
    else:
        for i in range(1000000):
            if (i % denominador == 0) and (i != 0):
                multiplos.append(i)
        print(multiplos)


if __name__ == '__main__':
    multiplos_2()
