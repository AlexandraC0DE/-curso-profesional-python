# Al trabajar con listas puedes hacer uso de 
# las sublistas

lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
#                  0         1         2       3       4        5

# Para generar una sublista vamos a colocar
# el indice inicial y el indice final 
#  [start:end]

sub_lista = lista_cursos[1:4]
# print(sub_lista)

# [start:] -> obtenemos los últimos elementos de la lista
# a partir del indice que hayamos indicado
sub_lista = lista_cursos[1:]
# print(sub_lista)

# [:end] -> para obtener los primeros elementos 
# de la lista hasta el indice que hayamos indicado
sub_lista = lista_cursos[:4]
# print(sub_lista)

#Generar sublista a partir de saltos de 2 en 2
# [start:end:skip]
sub_lista = lista_cursos[1:5:2]
# print(sub_lista)

# también se pueden obtener los elementos con saltos de 2 en 2
# sin indicar el indice inicial o final
# ejemplo
sub_lista = lista_cursos[::2]
# print(sub_lista)
sub_lista = lista_cursos[::-2] # se invierte la lista para comenzar de derecha a izquierda
print(sub_lista)
