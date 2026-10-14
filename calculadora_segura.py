def calculadora_segura(texto_a, texto_b, operacion):
    try:
        num_a = float(texto_a)
        num_b = float(texto_b)
    except ValueError:
        return "Error: valor no numérico"

    try:
        if operacion == "suma":
            return num_a + num_b
        elif operacion == "division":
            return num_a / num_b
        elif operacion == "resta":
            return num_a - num_b
        elif operacion == "multiplicacion":
            return num_a * num_b
    except ZeroDivisionError:
        return "Error: división entre cero"