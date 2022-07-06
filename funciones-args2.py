from itertools import combinations


def promedio(*args):
    return sum(args) / len(args)

# p4=500 es un parametro opcional
def combinacion(p1, p2, *args, p4=500):
# cuando nuestro porgrama posea 2 o más funciones
# hay que separar las funciones mediante 2 saltos
# dos saltos deben encontrarse entre función y función
# esto para poder leer bien nuestro código y siguiendo
# las convenciones de los desarrolladores python


    print(p1)
    print(p2)
    print(args)
    print(p4)

# Los argumentos se han asignado según su posición
# el primer rgumento (p1) para el primer parametro (10)
# el segundo argumento (p2) para el segundo parametro (20)
# el tercer argumento (p3) para el tercer parametro (1)
# para que un parametro opcional no se adhiera a la tupla
# simplemente hayq ue renombrarlo
# los parametros opcionales son los que ya poseeen un valor
combinacion(10, 20,1, 2, 3, 4, 5, 6, 7, 8, 9, 0, p4=1000)

