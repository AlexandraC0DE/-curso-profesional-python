# Para que nuestras funciones retornen valores
# podemos hacer uso de la palabra return
# las funciones en Python nos permiten retornar multiples valores
# lo mejor es no retornar más de 3 valores.

def suma(n1, n2):
# Al Python visualizar que intento retorna 2 valores va 
# a devolver una tupla con ambos valores
# en ese caso se puede implementar el desempaquetado de tuplas
# para generar nuevas variables para los valores retornados
    return  n1 + n2, 'La función retorna 2 valores'

numero_uno = int(input('Ingresa el primer número entero: '))
numer_dos = int(input('Ingresa el segundo número entero: '))

# Para desempaquetar el resultado, crearé otra variable
resultado, mensaje = suma(numero_uno, numer_dos)
print('El resultado es:', resultado)
print(mensaje)

# _ -> Omitir valor