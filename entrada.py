# Valores de entrada
# obtener valores que el usuario a ingresado a través de su teclado
# La función input siempre va a retornar un string, es decir una cadena de caracteres 
full_name = input('Ingresa tu nombre completo: ')

# print(full_name) 
# print(type(full_name)) 

# La función input va a deter la ejecución del programa hasta que se precione enter
# una vez se preione enter la función va a retornar los valores que el usuario ha ingresado
# Vía teclado


# para trabajar diferentes tipos de datos
# para crear un valor d enúmeor entero hay que usar la función int()
# con esto serás capaz de generar un tipo entero a partir de un str
age = int(input('Ingresa tu edad: '))

# Para generar un tipo float a partir de un string hay que usar la función float()
tall = float(input('Ingresa tu altura: '))

# Obtener un tipo booleano a través de lo que el usuario ingresó
# a través del teclado
autoritation = input('¿Autorizas el programa? (si/no)') == 'si' 

print(full_name) 
print(age) 
print(tall) 
print(autoritation) 


# de esta forma podemos leer lo que el usuario ingresó a través del teclado