print("Hola Mundo")

saludo = "Miarma que cosa más grande el pytón"
def saludar():
    # global sirve para modificar una variable dentro de un método a nivel global
    global saludo
    saludo = "Hola a todos"
    print(saludo)

saludar()

print (saludo)

def saludarV2():
    return saludo

# Esto es un doble return, donde puedes guardar los valores en distintas variables.
def coord(ciudad):
    if ciudad == "Sevilla":
        return 38.1234, -6.4567
    else:
        return 0,0

#lat, lng = coord("Sevilla")
lat, lng = coord("Cádiz")

#Investigar sobre los valores por defecto de los métodos.

print(lat)
print (lng)

# El orden en el que le pases los parámetros no importa
def suma(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado

print(suma(30,7))
print(suma(1,2,3,4,5,6,7,8,9))

#Argumentos indeterminados

def indeterminados_nombres(**kwargs):
    print("Mira tú: ", kwargs["n"])
    for kwarg in kwargs:
        print(kwargs, "=>", kwargs[kwarg])

indeterminados_nombres(n=5, c="hola", l=[1,2,3,4,5])



