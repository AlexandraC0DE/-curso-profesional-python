# Buscar strings dentro de otros strings
# Utilizando el método count sabremos si un string, existe dentro de otro string
# a demás de saber cuántas veces se repite ese strings
title_course = 'Curso profesional de Python, dónde aprenderemos Python'
counter = title_course.count('x')
print(counter)

# También podemos buscar un string dentro de otro string con la palabra reservada in
# la palabra reservada in nos va a retornar un valor booleano
# dependiendo de si el elemnto a buscar se encuentra o no en el string
# si escribismos toda la palabra Python en minuscula y no está escrito de esa forma
# en nuestro string Python lo tomará como false
# sin embargo con el método lower podemos convertir todo el texto en minuscula
# print('python' in title_course.lower())
# print('codigofacilito' not in title_course.lower()) negar
# print('Python' in title_course)

# startswith nos permite conocer si un string se encuentra al inicio de otro string
# el método startswith  va a retornar un valor booleano
# print(title_course.startswith('Curso'))

# el método endswith seremos capaces de conocer si un string finaliza con otro string
print(title_course.endswith('Python'))
