# En Python podemos justificar y alinear los strings
# ljust -> nos permitirá justificar a la izquierda
# rjust -> justificar a la derecha
# center -> centrar
# Estos métodos no modifican al string original, a parti de él se genera uno nuevo
# recuerda que los strings en Python son objetos inmutables
message = 'Hola mundo' 
message = message.center(20)

print(message)