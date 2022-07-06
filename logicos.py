# Operadores lógicos
# Nos permiten comparar tipos de datos booleanos
# ellos son: and , or y not

# and
# todas las comparaciones deben ser verdaderas
#para que el resultado final sea verdadero
# si una sola comparación es falsa el resultado final sera falso
result_final = True and True and False
print(result_final)

result_final2 = True and True and 100 > 20
print(result_final2)

# or
# por lo menos una de las comparaciones debe ser verdadera
# para que el resultado final sea True
result_final3 = False or False or 100 > 20
print(result_final3)
# al utilizar parénstesis es posible combinar los operadores lógicos
# podemos combinar operadores lógicos utilizando parentesis,
# lo cual no permitiría generar comparaciones mucho más complejas
result_final4 = True and ( False or 5 > 10 )
print(result_final4)


# not
# este operador nos permite negar un valor booleano
# convierte true a false y viceversa, convierte false a true
result_final5 = not True #verdadero se niega, resultado false
print(result_final5)

result_final6 = not False #falso se niega, resultado True
print(result_final6)


