# para conocer el indice de los elementos de una lista
# nos podemos apoyar del metodo index

lista = [ 8, 90, 1, 5, 44, 132, 600, 3, 4 ]

print(5 in lista)

index = lista.index(5)
print(index)

# si existiesen 3 números iguales, el método index 
# va a retornar el primer indice encontrado
# al intentar obtener el indice de un número que no existe
# obtendremos un error
# por ello es mejor asegurarnos que un elemento se encuentra dentro de una lista
# para evitar errores