
# Al igual que con las listas, con las tuplas trabajaremos mediante índices esto para
# poder obtener los valores almacenados
#            -5        -4       -3        -2       -1
cursos = ('Python', 'Flask', 'Django', 'Rails', 'MongoDB')
#            0         1        2        3         4

# para obtener algún elemento de la tupla lo haremos a través de índices
primer_curso = cursos[-2]
print(primer_curso)

#Para crear una subtupla basta con indicar 
# el índice inicial y el índice final
# sub_tupla = cursos[0:3]
# sub_tupla = cursos[:3]
sub_tupla = cursos[:] # generar una sub tupla con todos los elementos de la tupla original
print(sub_tupla)

