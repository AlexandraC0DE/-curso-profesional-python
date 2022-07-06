# Comprimir elementos para generar tuplas
# si alguna de estas estructuras no posee la misma cantidad de elementos que otras
#  los valores restantes serán omitidos, ya que la combinacion entre 
# tupla y lista debe ser exacta

lista = [1, 2, 3, 4, 5, 6, 7]

tupla = (10, 20, 30, 40, 50)

tupla_2 = (1000, 2000, 3000, 4000, 5000)

lista_2 = [100, 200, 300, 400, 500]

# Utilizando la función zip combinaremos las valores de la lista y de la tupla

result = zip(lista, tupla, lista_2, tupla_2) # -> zip
# a partir del objeto zip seremos capaces de generar una nueva tupla
result = tuple(result) # se puede trabajar list(result) pero lo aconsejable es trabajar siempre con tuplas
print(result)
# al ejecutar puedes ver que la tupla almacena sub tupla
# cada una de estas subtuplas es la combinación de los elementos de 
# nuestra lista y de nuestra tupla

