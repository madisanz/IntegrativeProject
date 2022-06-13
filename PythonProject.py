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
   -> Vanesa Paola Soria    E-mail: vanesa.soria.p@gmail.com
   -> Lucia Anahi Roldan    E-mail: luciardna@gmail.com
   ->
   
'''


#Definimos una lista vacia
lista=[]

#El usuario ingresa los 5 numeros enteros
for x in range(5):
    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)

#Imprimimos la lista
print(lista)