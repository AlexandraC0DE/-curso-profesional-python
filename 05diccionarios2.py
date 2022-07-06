# los diccionarios son mutables se les puede añadir y eliminar 
# cualqueir tipo de dato
# a diferencia de las listas y de las tuplas los diccionarios no se rigen 
# por la regla de los indices
# los diccionario corresponden a una llave no a un índice
# todos los valores necesitan tener una llave y cada llave necesita tener un valor
# una llave puede ser cualquier tipo de objeto inmutable en Python
# ya sea un string, un booleano, un entero o un flotante, una tupla. etc...
# en Python no se permiten llaves duplicadas
# y el valor de la llave que va a tomar python es el ultimo valor duplicado
#  de la llave asignada

# añadir elementos al diccionario
element = {'a': 1, 'b':2, 'c': 3, 'a':4}
'''
#   llave tipo nombre  valor
element['nombre'] = 'Cody'  #objeto inmutable // se crea la llave con su valor
#   llave tipo tupla
element[(1, 2, 3)] = 'La llave es una tupla'

# se Actualiza el valor que la llave 
element['nombre'] = 'Codigofacilito' 

#  Para saber número elementos de un diccionarios usamos len
print(len(element))
print(element)
'''