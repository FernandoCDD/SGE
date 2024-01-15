
def cargar_palabras():
    fichero = open('ejercicio1/palabras.txt', 'r')
    palabras = fichero.readlines()
    fichero.close()
    return palabras

def mostrar_palabras():
    lista_palabras = cargar_palabras()
    lista_bien = [lista_palabras.rstrip('\n') for lista_palabras in lista_palabras]
    return lista_bien

def mostrar_palabras_frecuencia():
    lista = mostrar_palabras()
    frecuencia = {}
    for palabra in lista:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

print ("Que desea hacer?")
print ("1. Importar palabras clave")
print ("2. Mostrar palabras clave *20")
print ("3. Mostrar palabras clave con frecuencias")
print ("4. Salir")

opcion = 0

while opcion != 4:

    opcion = int(input("Introduzca una opcion: "))

    if opcion == 1:
        cargar_palabras()
        print("Palabras importadas")
    elif opcion == 2:
        print(mostrar_palabras() * 20)
    elif opcion == 3:
        print(mostrar_palabras_frecuencia()) 
    elif opcion == 4:
        print("Adios máquina")

    else:
        print("Opcion incorrecta")
