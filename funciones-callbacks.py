# los callbacks son funciones utilizadas como argumentos para otras funciones
# y serán las funciones que reciban estos argumentos las cuales las llamen
# lOS CALLBACKS SON de mucha utilidad sobre todo en programas modularizables

promedio = lambda *args : sum(args) / len(args) # funcion calcula promedio

aprobatorio = lambda calificacion : calificacion >= 7 # función saber si aprobó la materia

def es_aprobatorio(calificacion):
    return calificacion >= 90


def mostrar_mensaje (func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f'felicidades, aprobaste la materia con {promedio}')
    else:
        print('No aprobaste la materia.')

mostrar_mensaje(promedio, es_aprobatorio, 10, 10, 8, 7, 7 )

# print(promedio(10, 10, 9, 8, 7))
# print(aprobatorio(4))