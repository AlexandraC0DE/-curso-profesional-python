# un closures es una función que puede generar de forma dinamica a otra función
# y esta nueva función puede acceder a la variables locales aún
# cuando la primera haya finalizado

def saludar(username):
    mensaje = f'Hola {username}' # Variable local


    def mostrar_mensaje(): # Anidada
        print(mensaje)
    
    return mostrar_mensaje

username = 'Cody'
respuesta = saludar(username)

respuesta()

# en este caso la función saludar es un closures una función que retorna otra función
# y a su vez esta nueva función puede acceder a las variable locales, 
# aún cuando la primera haya finalizado.
# De cierta manera esta nueva función tiene memoria
# pudiendo recordar y acceder a las variables locales que fueron creadas en scopes superiores