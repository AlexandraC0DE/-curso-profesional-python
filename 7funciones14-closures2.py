#En Python Las funciones son ciudadanos de primera clase
# esto quiere decir que funciones pueden retornar funciones
# funciones pueden ser asignadas a variables
# funciones pueden ser utilizadas como argumentos
# funciones pueden retornar otras funciones

# esta función tendrá a su vez una función anidada
def saludar():

    def mostrar_mensaje():
        print('Hola nos encontramos en el curso de Python.')
# Ahora hagamos que nuestra función saludar retorne a la función mostrar_mensaje
    return mostrar_mensaje

respuesta = saludar()
print(respuesta)
print(type(respuesta))

# para llamar a una función dentro de una variable
respuesta()