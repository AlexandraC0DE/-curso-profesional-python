# para concoer que llaves y que valores almacenamos en los diccionarios
# los siguientes e métodos nos ayudarán en este problematica

# keys -> llaves
# values -> valores
# items -> elementos

diccionario = {'a': 1, 'b': 2, 'c': 3, 'd':4}
# llaves = diccionario.keys()

# este método va a retornar un objeto dónde se encuentran almacenadas
# todas las llaves del diccionario
# el objeto retornado podemos convertirlo en una tupla
llaves = tuple(diccionario.keys()) # es más seguro trabajar con una tupla de llaves
print(llaves)

valores = tuple(diccionario.values())
print(valores)

elementos = tuple(diccionario.items())
print(elementos)

# es buena idea convertir los objetos a tuplas para que posteriormente nuestro programa no
# pueda modificarlos y no existan posibles errores

