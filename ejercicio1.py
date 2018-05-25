# Ejercicio1
# A partir de los arrays x y fx calcule la segunda derivada de fx con respecto a x. 
# Esto lo debe hacer sin usar ciclos 'for' ni 'while'.
# Guarde esta segunda derivada en funcion de x en una grafica llamada 'segunda.png'

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = np.linspace(0,2.,10)
f = np.array([0., 0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.])
x = x[1:]
d1 = (f[1:] - f[:-1])/(x[1]-x[0])
x = x[1:]
d2 = d1[1:] - f[:-2]/(x[1]-x[0])
plt.figure()
plt.plot(x, d2)
plt.xlabel("X")
plt.ylabel("Segunda derivada")
plt.savefig("segunda.png")





