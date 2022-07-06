# estaremos trabajando con dos funciones que utilizaremos mucho con el ciclo foreach
# me refiero a la funcion range y a la función enumerate

# la función range nos permitirá crear una secuencia de numeros enteros
# los cuales facilmente podemos iterar
# creemos un rango del 0 al 10
# range por default comenzará en 0 y finaliza al partir del valor que hayamos colocado 
# menos 1

# rango = range(21) # 0 - 10

# for valor in range(21):
#     print(valor)

# si no queremos comenzar de 0, si queremos comenzar a partir de un numero diferente
# en esos casos sepamos que debemos colocar dos argumentos a la función range
# que sería el punto inicial y el punto final de dónde queremos partir y donde
# queremos finalizar

# for valor in range(5, 21):
#     print(valor)

# si lo deseas también puedes colocar un tercer argumento
# este tercer arguimento hace referencia a los saltos
# por ejemplo creemos un rango de numero enteros 
# for valor in range(5, 21, 3):
#     print(valor)

# al igual que con las sublistas, la función range opcionalmente puede 
# trabajar con 3 argumentos, que sería el punto inicial start = 0,
# el punto final end y los saltos skips.

# Para la función enumerate
# voy a iterar utilizando índeces utilizando enumerate, que nos permite enumerar
# cada uno de los elementos de una colección
numeros = [ 10, 20, 30, 40, 50]
# dentro del parentesis de la función enumerate pasamos como argumento 
# la variable numeros o nuestra colección
# la función enumerate va a retornar una tupla con dos valores
# el primer valor hace referencia al indice del elemento de la colección
# y el segundo valor hace referencia al elemento percé de la colección
# for indice, numero in enumerate(numeros):
#     print(indice, numero)

# la función enumerate nos va a retornar un elemento retornable que a su vez
# posee tuplas, estas tuplas van a almacenar dos valores
# el primer valor hace referencia al indice del elemento de la colección
# y el segundo valor hace referencia al elemento percé el cual estamos iterando

# también es posible modificar el valor del indice
# basta con pasar como argumento un segundo valor a nuestra funcion
# que sería el número a partir del cuál queremos comenzar  
# que por default es 0 pero si nosotros quisieramos comenzar con 10 podemos hacerlo
# for indice, numero in enumerate(numeros, 10):
#     print(indice, numero)
# aunque esto no es algo muy común

for indice, numero in enumerate(numeros):
    print(indice, numero)