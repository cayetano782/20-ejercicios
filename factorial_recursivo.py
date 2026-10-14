def factorial_recursivo(n):
    if n <= 1:
        return 1
    return n * factorial_recursivo(n - 1)