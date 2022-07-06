# existen dos palabras las cuales nos permitirán cambiar el comportamiento de nuestro ciclos
# ya sea un ciclo while o un ciclo foreach
# me refiero a brake and continue

titulo_curso = 'curso profesional de Python'

for caracter in titulo_curso:
    
    if caracter == ' ':
        # break nos permite finalizar de forma inmediata la ejecución de nuestro ciclo
        continue # lo único que hace es pasar a la siguiente iteración

    print(caracter)
