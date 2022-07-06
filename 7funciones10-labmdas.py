# En Python las funciones son ciudadanos de primera clase
# o también conocidas como ciudadanos de primer orden
# quiere decir que las funciones pueden ser asignadas a variables
# pueden ser utilizadas como argumentos para otras funciones 
# e incluso funciones pueden retornar funciones

def centigrados_a_farhenheit(grados):
    return grados *1.8 + 32

#cuando no sepamos cuando utilizar una función lo mejor es almacenarla en una
# variable y a partir de dicha variable, hagamos el video bajo demanda
# para ello podemos hacer lo sigguiente, declaramos la función y posteriormente
# le asiganamos el nombre de la funcíon la cuál queremos almacenar
mi_funcion = centigrados_a_farhenheit
print(type(mi_funcion))
# ahora para poder llamar a la funcion lo haremos a través de la avriable
print(mi_funcion(10))


# nosotros podemos llamar una función n cantidad de veces
# siempre y cuando sepamos cuando utilizarla
# print(centigrados_a_farhenheit(10))
# print(centigrados_a_farhenheit(-1))
# print(centigrados_a_farhenheit(8))