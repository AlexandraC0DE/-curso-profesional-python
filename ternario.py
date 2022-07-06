calification = 10
# color = None

# if calification >= 7:
#     color = 'verde'
# else:
#     color = 'Rojo'

# equivalente al operador ternario en Python
# color es igual a verde si y solo si la claificación es
# mayor o igual a 7 de lo contario el color ser'a rojo
# el else es opcional sin embargo cuando estamos condicionando sobre
# una sola línea de código el else se convierte en obligatorio
# si eliminas el else que está acá abajo el programa dará un error
color = 'Verde' if calification >= 7 else 'Rojo'

print(calification, color)