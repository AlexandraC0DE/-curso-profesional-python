# Attrs de clase son atrubutos los cuales le pertenecen a una clase y para utilizarlos
# tenemos que utilizar dicha clase
# Attrs de instancia son los atributos que le pertenecen a un objeto y para que podamos utilizarlos
# obligatoriamente trabajaremos con el objeto

# para crear atributos de clase, basta con definir variables dentro de la clase
# estos atributos le pertenecen a la clase y para que nosotros podamos 
# utilizarlos obligatoriamente haremos uso de la clase
class Usuario:
    username = 'Alexa'
    email = ''

Usuario.username = 'User1'
Usuario.email = 'User1gmail.com'

print(Usuario.username)
print(Usuario.email)