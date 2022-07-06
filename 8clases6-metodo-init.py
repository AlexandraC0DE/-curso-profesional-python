# la mejor forma de definir e inicializar un objeto en Python haremos
# uso del método __init__

# de esta forma estamos estandarizando los objetos, objetos que poseen un mismo tipo de clase
# el método __init__ se va a ejecutar siempre que nosotros creemos un objeto
# de la clase, no solo nos permite definir que atributos tendrá el objeto
#  si no que trambién nos permite inicializarlos, para ello trabajaremos con parámetros

class Usuario:
    # Object
    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

# al momento de crear estos objetos, estamos definiendo e inicializando sus atributos
user1 = Usuario('user1', 'password1')
user2 = Usuario('user2', 'password2')
user3 = Usuario('user3', 'password3')
user4 = Usuario()

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(user4.__dict__)

'''
Repaso:

En python nosotro podemos añadir atributos (Attrs) a nuestros objetos
de forma dinámica, si queremos utilizar un atributo que no existe dentro de un objeto
entonces Python lo que hará es buscar el atributo dentro de la clase, para poder utilizar el
atributo de clase y si el attrs no existe Python lanzará un error.

Siempre que creemos atributos para nuestro objeto, estos atributos se van a añadir en el
meta-atributo __dict__ atributo que como podemos observar es un diccionario.
Y para poder estandarizar los nombre y la cantidad de atributos que poseerán nuestros objetos
haremos uso del método __init__

El método init se va a llamar cuando, el objeto sea instanciado y mediante este método seremos
capaces de definir, la cantidad y nombres de atributos, que poseerán los objetos
de igual forma podemos inicializarlos, utilizando parámetros y al momento de crear el objeto
se colocan los correspondientes argumentos.

'''