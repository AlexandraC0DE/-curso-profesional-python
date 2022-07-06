# aprenderemos a estandarizar atributos
# Attrs de clase
# Attrs de instancia
# el parámetro self es una palabra reservada que hace referencia a sí mismo
# este término es utilizado por convención de la comunidad Python 
class Usuario:
# sin embargo, es posibile inicializar los atributos con otro tipo de 
# argumentos veamos

# la mejor forma de inicializar un objeto en Python es con el método __init__

    def inicializar(self, username, password): # self hace referencia al objeto percé
# de forma dinámica en tiempo de ejecución se van a añadir los 
# siguientes atriubutos al objeto user1 y user2
        # añadiendo Attrs al objeto
        # self.username = ''
        # self.password = ''
        self.username = username
        self.password = password

# todos los objetos van a tener 2 atributos username y password siempre y cuando
# se llame a inicializar

user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

# estos atributos se añaden al objeto al momento de llamar al método inicializar
# como el objeto posee el parámetro self no vamos a llamar a ningún atributo
# ya que el parámetro será el objeto y como el objeto ya está definido no hay necesidad
# de colocar ningún argumento
# user1.inicializar('user1', 'Password1')
# user2.inicializar('user2', 'Password2')
# user3.inicializar('Cody', 'Password3')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

# recuerda que cuando python está asignando un attrs que no existe dentro del objeto
# entonces se procede a añadir dicho attrs al objeto

