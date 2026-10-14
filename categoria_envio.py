def categoria_envio(peso_kg):
    if peso_kg <= 1:
        return "Sobre"
    elif peso_kg <= 5:
        return "Paquete pequeño"
    elif peso_kg <= 20:
        return "Paquete grande"
    else:
        return "Voluminoso"