# __doc__ (Módulos, Clases, Métodos y Funciones)
# por convención el docstring se va a crear utilizando triple comillas """ """
# para testearlo en consola utilizamos python -m doctest funciones-testear.py
def suma(numero_1, numero_2):
    """
    La función suma 2 números enteros.
    Argumentos:
    numero_1(int)
    numero_2(int)

    Se retorna la suma de los parámetros

    >>> suma(10, 20)
    30

    >>> suma(100, 200)
    300

    """
    return numero_1 + numero_2

def resta(numero_1, numero_2):
    """
    >>> resta(100, 200)
    -100
    """
    return numero_1 - numero_2
