# Ejercicio 2
# Complete el siguiente codigo para recorrer la lista `x` e imprima
# los numeros impares y que pare de imprimir al encontrar un numero mayor a 800
import numpy as np

x = np.int_(np.random.random(100)*1000)
a = 0
print(x)
for i in range(len(x)):
    if (a == 0):
        if(x[i] % 2 != 0):
            print(x[i])
        if(x[i] > 800):
            a = 1




