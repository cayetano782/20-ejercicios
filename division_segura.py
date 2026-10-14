def division_segura(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: división entre cero"