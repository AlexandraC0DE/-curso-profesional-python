# a diferencia de otros lenguajes de programación Python permite la herencia multiple
# Quiere decir que una clase puede heredar de multiples clases
# lo cual tiene muchas ventajas

class Animal(): # Esta clase será la clase padre de la clase mascota 
    def comer(self):
        print('El animal come.')


    def dormir(self):
        print('El animal duerme.')

class Mascota(Animal): # Clase Padre
    pass

class Felino:

    def cazar(self):
        print('El felino caza.')

# Gato va a heredar de la clase mascota
class Gato(Mascota, Felino): # Clase Hija
    pass

patricio = Gato()

patricio.comer()
patricio.dormir()

patricio.cazar()

# Las clases Padre pueden convertise en clases Hija, 
# estas clases de igual forma pueden heredar de otras clases

'''
Recordemos:
En Python es posible implementar la herencia multiple, podemos hacer que una clase
herede de multiples clases, para ello solo basta con colocar dentro de los parentesis
separadas mediante una coma, todas aquellas clases de las cuales queremos heredar

Por último también recuerda que las clases padre también pueden heredar de otras clases

'''
