
# el alcance que tiene una variable depende totalmente de su scope, dónde fue creada
# si la variable fue creada fuera de un bloque la conoceremos como variable global
# una variable global puede ser utilizada en cualquier parte del programa
# ya sea dentro de bloques o fuera de bloques

# las variables que fueron creadas dentro de algún bloque unicamente podrán ser utilizadas 
# dentro de dicho bloque, una vez el bloque finalice, todas las variables que fueron creadas
# dentro de él serán destruidas y no podremos utilizarlas fuera del bloque.


# ahora veremo como se comportan las variables 
# tanto dentro como fuera de las funciones
animal = 'León' # variable global, fueron creadas fuera de un bloque
# las variables globales pueden ser utilizadas dentro de 
# cualquier bloque, ya se sea un bloque dentro de una función,
# una condición o un bloque de un ciclo

def imprimir_animal():
# Para modificar el valor de una variable global dentro de un bloque
# haremos uso de la palabras reservada global
# esta se puede modificar dentro de una función

# indico que voy a utilizar la variable global y luego modifico su valor
    global animal
    animal = 'Ballena'

    # animal = 'Ballena' # variable local
# una variable local solo puedo ser utilizada en el bloque dónde fue creada
# variable local, solo funciona dentro de un bloque

    print(animal)
    print(id(animal))

imprimir_animal()

print(animal)
print(id(animal))

# las variables de este ejemplo se encuentran en scopes diferentes
# por lo tanto poseen alcances diferentes y es por eso que al 
# imprimir en consola aparecen ambas valores

# la principal diferencia entre una variable global y una variable local
# es su alcance dónde sí y dónde no pueden ser utilizadas
# Una variable global puede ser utilizada dentro de cualquier blooque y fuera de ellos
# por otro lado una variable local puede ser utilkizada unicamente en el bloque dónde fue creada
