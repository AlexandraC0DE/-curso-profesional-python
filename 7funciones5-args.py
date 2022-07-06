# las funciones en Python pueden recibir N cantidad de argumentos
# crearé un función la cual me permita calcular un listado de números enteros

# al colocar el * le estamos diciendo a Python que genere una tupla con esos
# argumentos, tupla la cual se va a asignar al parametro que tenga *
# todos aquellos parametros que posean * deben llamarse *args
# def promedio(*listado): # el * va pegado del parametro (por convención comunidad Python)
def promedio(*args):
# con el siguiente código podemos conocer el promedio de un listado de numeros enteros
    print(args)
    print(type(args))
    return sum(args) / len(args)

# si ya no queremos colocar un listado, si no que queremos colocar directamente 
# N cantidad de argumentospara concoer su promedio
# resultado = promedio([10, 10, 5, 7, 10])
# al eliminar [] e imprimir en consola nos arroja un error
# ya que en la cunción promedio solo hemos declarado un argumento
# y no 5 como lo muestra acá abajo
# en ese caso, en la función def promedio(listado) antepondremos
# un * quedando así (*listado):
resultado = promedio(10, 10, 5, 7, 10,10, 10, 5, 7, 10,10, 10, 5, 7, 10)
print(resultado)