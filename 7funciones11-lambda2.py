# una función lambda también conocida como una función ánonima
# es una función que se expresa en una sola línea de código
# a demás de no poseer un nombre, ya que por lo general 
# este tipo de funciones realizan tareas muy pequeñas

# lambda una función que se expres sin nombre y en una sola línea de código
# lambda <parámetros> : <cuerpo de la función>

funcion_grados = lambda grados : grados * 1.8 +32 # parametros obligatorios

print(funcion_grados(10))

# La función lambda se puede complicar utilizando más o menos parámetros

'''
estructuras comunes funciones lambdas:
sin_parametros = lambda : True (sin parametros)
parametros_default = lambda p1=10, p2=20, p3=30, : p1 + p2 + p3 ( parametro por default)
asterisco = lambda *args, **kwargs: len(args) + len(kwargs) (parametros que utilizan asterisco o doble asterisco )
'''