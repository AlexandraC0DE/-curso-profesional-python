'''
Una muy buena práctica al trabajar con funciones es que la documentemos
para ello utilizaremos el Docstring
un Docstring es un comentario que se coloca en la primera línea de código de nuestra función
el docstring será almacenado en atributo __doc__ de nuestra función
'''

# __doc__ (Módulos, Clases, Métodos y Funciones)
def suma(numero_1, numero_2):
    """
    La función suma 2 números enteros.
    Argumentos:
    numero_1(int)
    numero_2(int)

    Se retorna la suma de los parámetros

    TODO:
        *
    """
    return numero_1 + numero_2

# print(suma.__doc__)
print(help(suma))