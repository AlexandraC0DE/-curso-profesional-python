'''
un generador es un tipo especial de función la cual retorna objetos
sin que esta finalice
'''

def pares(): # generador -> lasy iterator
    # es decir trabajaremos con una iteración perezoza
    # pudiendo así obtener cada uno de los objetos que el generador genera y retorna on demand
    # bajo demanda, siempre que lo necesitemos
    for numero in range(0, 100, 2):
        # la palabra reservada yield nos permite retornar valores sin que la función finalice
        # a diferencia de la palabra reservada return
        yield numero # después de retornarse la función suspende su ejecución
        # print(numero)

        print('se reanuda la ejecución')

# en este caso en cada iteración la función retorna y pausa su ejecución 
for par in pares():
    print(par)