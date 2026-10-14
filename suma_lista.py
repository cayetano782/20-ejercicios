def suma_lista(numeros):
    if not numeros:
        return 0
    return numeros[0] + suma_lista(numeros[1:])