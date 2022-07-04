'''pythonproject.py
Codificar en Python un programa que contenga las siguientes condiciones:
   -> El usuario debe ingresar 5 números enteros, los cuales serán almacenados en una
lista
   -> Función Suma
   -> Función Promedio
   -> Función Máximo
   -> Función Mínimo
Grupo: 
   -> Margarita Sánchez     E-mail: madisanz1@gmail.com
   -> Carla Argentina Wayar E-mail: carlaargentinawayar@gmail.com
   -> Lucia Anahi Roldan    E-mail: luciardna@gmail.com
   -> Jorge Daniel Rojas    E-mail: jorgedanielrojas20@gmail.com
   -> Ignacio Jose Rocha    E-mail: ignac1997nacho@gmail.com
   -> Antonella Roggio      E-mail: antonella.roggio5@gmail.com
   -> Emma Gutiérrez        E-mail: emygut@gmail.com
   
'''
#Definimos Función suma propia 
def suma (lista):
    total_suma=0
    for numero in lista:
        total_suma=total_suma+numero
    return total_suma

#Función promedio
def promedio(lista):
    promedio=0
    contador=0
    for i in range(len(lista)):
        promedio=promedio+lista[i]
        contador=promedio/len(lista)
    return contador

#Función máximo
def maximo(lista):
    grande=lista[0]
    for numero in lista:
        if numero>grande:
            grande=numero
    return grande

#Función mínimo 
def minimo(lista):
    minimo=lista[0]
    for numero in lista:
        if numero<minimo:
            minimo=numero
    return minimo

def main(lista):
    #Llamo a la Función suma propia
    Suma_total=suma(lista)
    print(" El resultado de la Suma es:  ",Suma_total, "\n")
    #Llamo a la Función promedio
    a=promedio(lista)
    print ( "El promedio de la lista es: " , a , "\n")
    #Imprimo el valor máximo
    print ("El valor MÁXIMO ingresado es: ", maximo(lista), "\n")
    #Imprimo el valor mínimo
    print ("El valor MÍNIMO ingresado es: ", minimo(lista), "\n")

#Definimos una lista vacia 
lista = []

#El usuario ingresa los 5 numeros enteros
for x in range(5):
    valor = int (input("Ingrese un valor entero:  "))
    lista.append(valor)

#Imprimimos la lista
print("Los numeros ingresados son: \n ",lista)
main()
