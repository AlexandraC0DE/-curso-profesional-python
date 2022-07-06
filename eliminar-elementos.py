
# eliminar elementos de un diccionario

diccionario = {'a':1, 'b':2, 'c':3, 'd':4}

# para saber la longitud del diccionario antes de eliminar el elemento
print(len(diccionario))

# forma sencilla de eliminar elementos de un diccionario
# eliminaré el elemento cuya llave sea a
# del diccionario['a']  
print(diccionario)

# existe el método pop que también sirve para eliminar
# el método pop va a retornar el valor de la llave
valor = diccionario.pop('b')
# para eliminar todos los elementos de un diccionario 
# haremos uso del método clear
diccionario.clear()
print(valor)
# # para saber la longitud del diccionario después de eliminar el elemento
print(len(diccionario))

# antes de eliminar cualquier elemento del diccionario
# hay que asegurarse que dicho elemento exista para evitar cualquier tipo de error en 
# la ajecución del programa
