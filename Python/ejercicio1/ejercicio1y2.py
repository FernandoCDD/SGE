
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

def mostrar_palabras_tres_en_tres():

    frecuencias = {"uno": 1, "dos": 2, "tres": 3, "cuatro": 4}
    contador = 0

    for palabra in frecuencias:
        print(f"{palabra} : {frecuencias[palabra]}")
        if (contador == 3):
            input("Pulse una tecla para continuar")
        contador = 0

    palabras = list(frecuencias)
    print(palabras)


print ("Que desea hacer?")
print ("1. Importar palabras clave")
print ("2. Mostrar palabras clave *20")
print ("3. Mostrar palabras clave con frecuencias")
print ("4. Mostrar palabras de tres en tres")
print ("5. Salir")

opcion = 0

while opcion != 5:

    opcion = int(input("Introduzca una opcion: "))

    if opcion == 1:
        cargar_palabras()
        print("Palabras importadas")
    elif opcion == 2:
        print(mostrar_palabras())
    elif opcion == 3:
        print(mostrar_palabras_frecuencia()) 
    elif opcion == 4:
        mostrar_palabras_tres_en_tres()
    elif opcion == 5:
        print("Adios máquina")
    else:
        print("Opcion incorrecta")
