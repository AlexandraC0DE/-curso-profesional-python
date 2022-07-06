# Attrs de instancia 

class Usuario:
    # Attrs de clase
    username = 'Username por default'
    email = ''

# en Python podemos añadir atributos a nuestro objeto en tiempo de ejecución
# para lograr esto Python trabaja con un meta atributo
# __dict__
user1 = Usuario()
# 1. - Verifica si el attr existe dentro del objeto
# 2.- Verifica si el attrs existe dentro de la clase -> Lectura
# 3.- Lanzar un error
# print(user1.username)
print(user1.username)

print(id(user1.username))
print(id(Usuario.username))

print(user1.__dict__) # Va a almacenar mediante un diccionario todos aquellos atributos que poseea nuestro objeto
