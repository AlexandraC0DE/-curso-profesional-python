'''
Con los generadores nosotros seremos capaces de implementar un lazy iterator(iteración perezoza)
podemos obtener cada uno de los objetos que el generador genera y retorna
confomre a nosotros lo vayamos necesitando
'''

'''
Un generador es un tipo especial de función que nos permite retornar valores
que facilmente podemos iterar, para ello utilizamos la palabra reservada yield
esta palabra reservada nos permite retornar un valor y suspender de forma momentanea
la ejecución de la función, no es nuevamente cuando el generador es nuevamente
llamado cuando la función se reanuda desde el punto dónde se quedó
'''
'''
Si intentamos obtener valores cuando el generador ya finalizó, vamos a obtener como error
un stop iteration, error que facilmente podemos manejar si trabajamos con un try y un except
'''

def pares(): # Generador -> Lazy iterator
    for numero in range(0, 12, 2):
        yield numero # La función suspende su ejecución

        print('Se reanuda la ejecución')

generador = pares()
# trabajaremos los errores con try y except
while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El generador finalizó')
        break

# generador = pares()

# print(next(generador)) # cada línea de cpodigo nos permite obtener un nuevo objeto del generador
# print(next(generador))
# print(next(generador))
# nosotro pudieramos ejecutar diferentes sentencias entre una obtención y otra
# print('Ejecutamos código entre un llamado y otro')
# print(next(generador))
