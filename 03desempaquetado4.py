#este sería un tip que podemos utilizar al momento de 
#trabajar con tuplas, podemos desempaquetarlas, descomprimirlas
# y asignar sus valores a variables

# si no conocemos el total de elementos de la tupla
# podemos hacer uso de *resto valores
# De esta manera estaremos indicando que a partir del número 4
# los valores se almacenen en la lista *resto_valores 
numeros = ( 1, 2, 3, 4, 5 , 6, 7, 8, 9, 10 )
uno, dos, tres, cuatro, *resto_valores = numeros

# * -> Lista
# _ -> Omitir valor

print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_valores)

# El asterísco * es muy importante, ya que denota listas
# quiere decir que cada vez que veas un prefijo * la variable es una lista
# en el ejemplo de arriba estamos creando una lista, a partir del resto de la tupla
# que no fueron desempaquetados, que no fueron asignados a nuevas variables

# Para indicarle a Python que no queremos trabajar con el resto de valores
# le decimos de la siguiente forma que no queremos trabajar con el resto de valores
uno, _, tres, cuatro, *_, nueve, diez = numeros
print(uno)
print(tres)
print(nueve)
print(diez)
# print(resto_numeros)