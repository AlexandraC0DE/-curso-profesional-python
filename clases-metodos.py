class Usuario:
    username = 'Alexa'
    email = ''

user1 = Usuario()
user2 = Usuario()

user1.username = 'User1'
user1.pasword = 'User1gmail.com'

print(user1.username)
print(Usuario.username)

user1.password = 'password'

print(user1.__dict__)
print(user2.password)
