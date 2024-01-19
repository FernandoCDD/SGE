class Cliente:

    def __init__(self, dni, nombre, apellidos):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)


c = Cliente ('123455', 'Fernando', 'Claro')

print(c)
print(c.nombre)
c.nombre = 'Pepe'
print(c.nombre)

c.email = 'fernando@gmail.com'
print(c.email)

c2 = Cliente('4321', 'Luismi', 'López')
# print(c2.email)

## __str__ es como el ToString de Java, los guiones bajos indican que son métodos especiales, con los __
## lo que hacemos es ponerle privacidad a la variable.
#Hacer ejercicios de bloque de funciones y POO.