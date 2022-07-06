
calification = 3

# si calificación es igual a 10 (utilizando el operador relacional == obtendremos un
# resultado booleano)
# colocamos if mi condición y posteriormente un nuevo bloque el cual
if calification == 8:
# queremos ejecutar cuando la condición se cumpla para ello haremos uso de identación 4 espacios
# si la calificación es igual a 10 escribiremos en consola
    print('Felicidades aprobaste la materia con una calificación perfecta')
# en caso de que la consición se cumpla vamos a imprimir otro mensaje
# para que el usuario visualice el mensaje adecuado de acuerdo a su calificación
# debemos evaluar otras condiciones
# para ello haremos uso de la palabra reservada elif
elif calification == 9 or calification == 8:
    print('Felicidades, aprobaste la materia')
elif calification == 7 or calification == 6:
    print('Aprobaste la materia')
else:
    print('Reprobaste la materia')

    # lAS CONDICIONES Se evaluan de forma descendente se van descartando una por una
    # de esta forma es como podremos evaluar multiples condiciones