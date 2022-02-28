

def decimal_a_binario(numero, base):
    binario_entero = ""
    binario_decimal = ""
    parte_entera = abs(int(numero))
    parte_decimal = abs(numero) - parte_entera

    while parte_entera > 0:
        residuo = int(parte_entera % base)
        parte_entera = int(parte_entera / base)
        binario_entero = str(residuo) + binario_entero

    if numero < 0:
        binario_entero = "-" + binario_entero

    if parte_decimal != 0:
        while parte_decimal > 0:
            residuo = parte_decimal * base
            binario_decimal = str(int(residuo)) + binario_decimal
            parte_decimal = abs(residuo) - abs(int(residuo))
        return binario_entero + "," + binario_decimal
    else:
        return binario_entero


if __name__ == '__main__':
    try:
        numero_ingresado = float(input("Ingresa un número decimal: "))
        base_ingresada = int(input("Ingrese la base del sistema: "))
    except (ValueError, SyntaxError):
        print("Error: El numero ingresado deve ser entero y la base un entero psoitivo")
    else:
        binario = decimal_a_binario(numero_ingresado, base_ingresada)
        print(f"El número {numero_ingresado} en base {base_ingresada} es: {binario}")
