import numpy as np
# Pedro Martinez NC 0093 Fecha = 22/oct/2026
# Ejemplos de numpy Numerical Python
print("---Espaciado linealmente en array---0093")
arre = np.linspace(start = 0,stop = 1 ,num = 10) 
print(arre)
print("---Matriz identidad en array---0093")
matrix=np.eye(4)
print(matrix)
print("---Generar numerosa al azar (Aleatorios) en 2D array---0093")
numale=np.random.random([3,4]) # genera 12 numeros aleatorios
print(numale)
print("---generar 9 numeros aleatorios entre 0 y 1---0093")
numale=np.random.random([3,3]) # genera 12 numeros aleatorios
print(numale)
#como generar 9 numeros aleatorios comprendidos entre 1 y 20 
#con numpy en un arreglo de 3 por 3
print("---generar 9 numeros aleatorios entre 1 y 20---0093")
arre = np.random.randint(1, 21, size=9).reshape(3, 3) # genera 12 numeros aleatorios
print(arre)
print("Pedro Martinez NC 0093")