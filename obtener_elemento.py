def obtener_elemento(lista, posicion):
    try:
        return lista[posicion]
    except IndexError:
        return "Error: posición fuera de rango"