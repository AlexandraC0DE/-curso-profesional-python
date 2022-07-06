# este tema se encuentra relacionado con el tema de las funciones anidadas y el
# tema alcance de las variables

e = 'e'

def funcion_principal():
    a = 'a' # Variable local
    b = 'b'


    def funcion_anidada():
        c = 'c' # variables locales
        # para modificar una variable que se encuentra en un scope superior
        # tenemos que hacer uso de la palabra reservada nonlocal seguido del nombre de la variable
        # que queremos modificar
        # de esta forma le vamos a decir a Python que no estamos creando una variable nueva
        nonlocal b 
        b = 'Cambio de valor'

        print(a)
        print(b)
        print(id(b))

        print(e)

    funcion_anidada()
        # print(c)
    print(b)
    print(id(b))


funcion_principal()