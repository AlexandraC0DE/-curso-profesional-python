# los  métodos más usados al momento de trabajar con strings
# son split y  join
# no son los únicos pero si los más utilizados 

#método split nos permite generar una lista a partir de un strings
# lenguajes = 'Python Ruby Java Rust C++ C'
# Por default el método split va a divir el string utilizando espacios,
# cada espacio indica un nuevo elemento, dentro del listado
# si el string estuviese divido por guiones - nuestro listado
# unicamente poseería un solo elemento ['Python-Ruby-Java-Rust-C++-C']
# ya que no hay espacios en el string y no hay forma de dividirlo
# sin embargo si se quiere divir el string a través de otros caracteres, podemos 
# hacerlo ejemplo: 
# listado_lenguajes = lenguajes.split('-')
# El método split va a dividir el string a través de todas las coincidencias que se encuentren dentro del string
# listado_lenguajes = lenguajes.split()

#Si noquieres dividir el string por todas las coincidencias y solo por un par
# el método split puede recibir un segundo valor
# esto le indica a python que queremos generar una lista unicamente dividiendo 2 veces
#listado_lenguajes = lenguajes.split('/-/*', 2)

#print(listado_lenguajes)


#método join nos permite generar un string a partir de una lista

lenguajes = ['Python', 'Ruby', 'Java', 'Rust']
# el método join va a unir cada uno de los elementos de la lista
# utilizando los caracteres que se encuentren dentro del string
# 'caracteres'.join(lenguajes)
# el método join va a retornar un string
string_lenguajes = ' '.join(lenguajes)
print(string_lenguajes)
#para confirmar el tipo podemos hacer uso del método type
print(type(string_lenguajes))