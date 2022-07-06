#                 -6        -5        -4      -3      -2      -1
lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
lista_cursos_2 = ['C', 'C++', 'Docker']
#                  0         1         2       3       4        5
print(len(lista_cursos))

# este metodo nos permite añadir elementos al final de nuestra lista
# Por lo tanto s eva incrementado la longitud de la lista
lista_cursos.append('MongoDB')
lista_cursos.append('C#')
lista_cursos.append('JavaScript')

# Para añadir un elemento a la lista en un indice en concreto
# haremos uso del metodo insert
lista_cursos.insert(1, 'Rails')
lista_cursos.insert(0, 'Pygame')

# para unir dos listas
lista_cursos.extend(lista_cursos_2)

print(lista_cursos)
print(lista_cursos_2)
# Para conocer la longitud de una lista 
# podemos hacer uso de la funcion len
print(len(lista_cursos))


# Eliminar elementos de una lista
print(lista_cursos)
lista_cursos.remove('MongoDB')
# Otra forma de eliminar elementos utilizando indices con la palabras reservada del
del lista_cursos[0]
# por último para eliminar todos los elementos de una lista
#hay que hacer uso del elemento clear
lista_cursos.clear()
print(len(lista_cursos))



