# al igual que con las condiciones y los ciclos 
# las funciones también pueden ser anidadas

def operacion(cantidad, balance, tipo='deposito'):

    def deposito(cantidad, balance):
        return cantidad + balance
    

    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None


    if tipo == 'deposito':
        return deposito(cantidad, balance)
    elif tipo == 'retiro':
        return retiro(cantidad, balance)
    
    # print(deposito(10, 20))
    # print(retiro(50, 30))

resultado = operacion(10, 30, 'deposito')
print(resultado)