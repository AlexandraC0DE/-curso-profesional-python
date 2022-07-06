# función para calcular el área de un cículo
# def area_circulo(radio, pi):
#podemos asignar un parámetro por default de la siguiente manera
# los parámetros que tengan valor por default siempre van a encontrarse a la derecha
def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2)

# si la función recibe como argumento un valor,
#entonces es utilizado dicho valor
# resultado = area_circulo(10, 3.14)
resultado = area_circulo(10)
print(resultado)

# el nombre de los argumentos se asigna según su posición.