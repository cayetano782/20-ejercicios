def invertir_texto(texto):
    if len(texto) <= 1:
        return texto
    return texto[-1] + invertir_texto(texto[:-1])