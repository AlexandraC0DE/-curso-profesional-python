'''
Este es uno de los temas más importantes, al momento de trabajar con POO
y consiste en que una clase hija puede modificar el comportanmiento de los métodos
la clase padre con la finalidad de que estos comportamientos 
se adecuen a las necesidades de la clase hija
'''

# vamos a modificar el comportamiento del método comer y el método dormir
# mientras una clase tenga mayor jerarquía más abstracta será esta
# y si una clase tiene menos jerarquía más concreta será la clase

class SerVivo:

    def dormir(self):
        print('EL ser duerme.')

class Animal(SerVivo): # Esta clase será la clase padre de la clase mascota 
    def comer(self):
        print('El animal come.')


    # def dormir(self):
    #     print('El animal duerme.')

class Mascota(Animal): # Clase Padre
# para sobreescribir un método, basta con volverlo a definir
    def comer(self):
        print('La mascota come')

class Felino:

    def cazar(self):
        print('El felino caza.')

class Gato(Mascota, Felino): # Clase Hija
    
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f'{self.nombre} come.')

    # def dormir(self):
    #     print(f'{self.nombre} duerme.')

patricio = Gato('Patricio')

patricio.comer()
patricio.dormir()

# patricio.cazar()