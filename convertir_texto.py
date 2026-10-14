def convertir_a_entero(texto):
    try:
        return int(texto)
    except ValueError:
        return "Error: no es un número"