def contar_vocales(palabra):
    contador=0
    vocal=["a","e","i","o","u","A","E","I","O","U"]
    for letra in palabra:
        if letra in vocal:
            contador = contador + 1
    return contador