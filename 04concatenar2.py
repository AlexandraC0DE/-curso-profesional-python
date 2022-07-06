# los strings en Python son inmutables
# quiere decir que una vez que definamos un string, no podremos 
# modificarlo en tiempo de ejecución y así se quedará por el resto
# del programa, habrá ocaciones en las que queramos modificar
# nuestros strings, peor como sabemos, esto no es posible.
# Lo que sí podemos hacer es generar strings a partir de otros

nombre = 'Alexandra Mariela'
apellido = 'García'

# full_name = nombre + apellido + ' González'

# full_name = 'Señora %s %s González.' %(nombre, apellido)

#                     placeholder
# full_name = 'Miss. {} {} {}.' .format(nombre, apellido, 'González')

# full_name = 'Miss. {nombre} {apellido_1} {apellido_2}.' .format(
#    nombre = nombre,
#    apellido_1 = apellido,
#    apellido_2 = 'González'
#    )

print(full_name)


