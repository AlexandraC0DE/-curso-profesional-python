# a través del operador lógico or seremos capaces de asignar valores a nuestras variables
# Python va a evaluar cada una de las opciones al utilizar el operador lógico or
# y va a asignar a la vfariable el primer valor verdadero con el cual se tope

# en este caso python va asignar a la variable el primer valor
# verdadero con el cual se tope
# rceuerda que la lectura es de izquierda a derecha
# quieres decir que en el siguiente caso la variable va a almacenar el string 'Cody'
# variable = 'Cody' or 'Codigofacilitio'
# si comparamos con un valor falso, codigofacilito será almacena como el valor de l avariable
# variable = '' or 'Codigofacilitio'
# recuerda que puedes trabajar con cualquier tipo de dato
# variable = '' or 0 or [] or True

listado = []
nombre = 'Cody'

'''
if listado: 
    variable = listado
else:
    variable = nombre
'''
variable = listado or nombre

print(variable)

# con el operador or seremos capaces de asignar valores a nuestra variable
# tomando  como primer valor el elemento que sea true 