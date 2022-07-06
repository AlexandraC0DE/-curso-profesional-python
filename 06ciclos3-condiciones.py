# estructuras de código
#condicionar nuestro programa haremos uso de la palabra reservada if

result = 15

# esta expresión da como resultado False pero como la condición no se cumple
# no aparece el mensaje en consola
# para hacer uso de la palabra reservada if 
# colocamos un valor booleano o una expresión que nos permita
# generar un valor booleano
# la condición se va a cumplir siempre y cuando el valor booleano sea verdadero
if result > 10 and result < 20 :
# por conveción de la comunidad python crearemos un nuevo bloque, identado con 4 espacios
    print('La variable cumple con la condición.')
# La palabra reservada else nos permite ejecutar un código siempre y cuando la condición no se cumpla
else:
    print('La condición no se cumplió :(')

# haciendo uso de la palabra reserva if y la palabra reservada else podemos
# condicionar bloques de código
# el else es completamente opcional