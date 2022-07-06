# otra forma de pasar varios parametros a una función es utilizando doble *
# aunque al hacer esto, estaremos dejando a un lado trabajar con tuplas
# y nos concentraremos en trabajar ocn diccionarios
# con el parametro (**kwargs) convertiremos cualquier parametro en un diccionario

def promedio(*args):
    return sum(args) / len(args)


def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))


def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)

combinacion(1, 2, 3, 4, 5, cody=True, curso= 'Pytohon')

# ahora vamos a llamar a la función
# para ello no vamos a colocar directamente los argumentos 
# si no que nos apoyaremos de parametros
# en este caso estoy llamando a la función pasando dos listas
# para dos parametros, los parametros son eduardo y fernando
# usuarios(eduardo=[10, 10, 8], fernando=[10, 9, 9])