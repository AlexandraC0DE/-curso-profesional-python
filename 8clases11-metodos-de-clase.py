'''
Al igual que con los attrs a los métodos los podemos clasificar en 2 tipos
1.-Métodos de instancia, métodos los cuales le pertenecen a los objetos
2.-Métodos de clase, métodos los cuales le pertenecen a la clase
'''
# Métodos de clase
# utilizaremos decoradores

class Circulo:
    
    pi = 3.141592

    @classmethod
    def area(cls, radio): # parámetro (cls) hace referencia a la clase
        return cls.pi * (radio ** 2)

resultado = Circulo.area(14)
print(resultado)