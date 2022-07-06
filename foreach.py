# en Python el ciclo for no es más que un ciclo foreach
# utilizando el ciclo for seremos capaces de iterar sobre casa uno de los elementos
# dentro de una coleción, dentro de un objeto iterable
# facilmente puede ser un string, una tupla, un diccionario, una lista,
#  un entero, un flotante o un booleano
# cualquier objeto iterable puede ser utilizado dentro del ciclo for

# ahora voy a mostrar en consola cada uno de los elemento de la lista
# Para no utilizar los indices, voy a utilizar el ciclo foreach
usuarios = ['usuario1', 'usuario2', 'usuario3', 'usuario4']
# escribimos la palabra for y creamos una nueva variable, 
# puedes usar el mismo nombr en singular
for usuario in usuarios:
    print(usuario)

# el ciclo foreach se comprende de 4 partes
# for una variable que tomará el nombre d ecada uno de los elementos de la
# colección(por cada iteración), in y el objeto el cual queremos iterar.
# dos puntos : y creamos un nuevo bloque con identación de 4 espacios.
# una vez terminados de iterar cada uno de los elementos de la colección el ciclo foreach finaliza.
# y como en este caso no hemos usado ningún tipo de ocndición 
# no es posible utilizar el else.