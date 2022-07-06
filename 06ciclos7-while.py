# el ciclo while nos permite ejecutar una n cantidad de veces
# un bloque de código, hasta que una condición se cumpla

# contador = 1

# while contador <= 10:
#     print(contador)

# contador = contador + 1

numero = 123456789
contador_digitos = 0

while numero >= 1:
    # contador_digitos = contador_digitos +1
    contador_digitos += 1

    numero = numero / 10
# con el ciclo while también podemos hacer uso de else, que por su puesto es opcional
else:
    print(contador_digitos)



# el ciclo while lo utilizaremos siempre y cuando no sepamos 
# la cantidad de iteraciones que vamos a realizar
# ya que el ciclo while se apoya de una condición
# y cuando se va a cumplir la condición a ciencia cierta no lo sabemos

