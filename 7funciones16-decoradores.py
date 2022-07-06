'''
uno de los futures que más se utiliza para trabajar en Python 
son los decoradores, a través d elos decoradores, seremos capaces de reducir líneas
de código duplicadas, haremos que nuestro código sea aún más legible, fácil de
testear, de mantener y por supuesto tendremos un código mucho más Pythonico XD
'''

'''
Un decorador es una función que toma como input como valor de entrada una funcion
y a su vez retorna otra funcion.
Al momento de trabajar con un decorador, estaremos trabajando por lo menos con 3 funciones,
el input, el output y la función principal 

a -> La función principal (Decorador)
b -> La función a decorar
c -> La función decorada

regularmente vamos a hacer uso d elos decoradores siempre que
querramos extender funcionalidades a una función
ya sea porque no podemos modificar una función o simplemente no queremos hacerlo

en este caso la función a va a recibir a la función b y dará como reusltado la función c
a(b) ->

de esta forma vamos a extender funcionalidades
'''

def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
        # print('Nos encontramos en la funcion c')
        print('>>> Antes del llamado')

        resultado = funcion_b(*args, **kwargs)
        # estamos extendiendo funcionalidades
        print('>>> Después del llamado')

        return resultado

    return funcion_c

@funcion_a
def saludar():
    print('Hola, nos encontramos en una función')

# saludar()
@funcion_a 
def suma(numero_1, numero_2):
    return numero_1 +numero_2

resultado = suma(10, 20)
print(resultado)

# suma(10, 20)