# Obtener elementos de un diccionario
# unicamente podremos obtener los valores de una llave
# mientras la llave exista
diccionario = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }

# print('z' in diccionario) # con este método evitarás que el programa de un error y sabrás si un elemento se encuentra dentro de un diccionario

# obtener el valor de la llave 4 que serí el literal d
# valor = diccionario['a']
# print(valor)

# utilizando el método get del diccionario seremos capaces de obtener el valor de una llave
# de forma segura
valor = diccionario.get('a', 'La llave no existe en el diccionario' )
print(valor)

# la contraparte del método get es setdefault
# en dado caso la llave no exista, se procederá a añadir al diccionario
valor = diccionario.setdefault('e', 5 )
print(valor)
print(diccionario)
