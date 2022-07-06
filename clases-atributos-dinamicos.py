# añadir atributos de forma dinámica
# Attrs de clase
# Attrs de instancia 

class Usuario:
    # Attrs de clase
    username = 'Username por default'
    email = ''

# __dict__
user1 = Usuario()
user2 = Usuario()
# 1. - Verifica si el attr existe dentro del objeto
# 2.- Verifica si el attrs existe dentro de la clase -> Lectura
# 3.- Lanzar un error

# Cuando pYthon nota que estamos asignando un valor a un attrs que no existe dentro 
# del objeto, entonces python procede a añadir de forma dinámica en tiempo de ejecución
# dicho atrubuto al objeto, en este caso username pasa a ser un attr de instancia 
# un attrs el cual le pertenece al objeto
# de esta forma es como nosotros podemos añadir nuevos attrs al objeto

user1.username = 'cody' # Añadimos el attrs al objeto
user1.password = '1234'
print(user1.username) # Attrs de instancia

print(id(user1.username))
print(id(Usuario.username))

user1.password = 'password'

print(user1.__dict__) 
print(user2.password) 