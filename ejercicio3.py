#Ejercicio3
# Los arrays `u` y `v` representan dos series en funcion del tiempo `t`.
# Grafique las dos series de datos en una misma imagen 'serie.png'
# Calcule la covarianza entre `u` y `v` e imprima su valor.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
t = np.array([0.,0.1,0.2,0.3,0.4,0.5,0.6, 0.8, 0.9])
u = np.array([12.,45.,6.,78.,34.,22.,-10.,31.,-27.])
v = np.array([3.,11.,1.3,37.,11.,6.,-23.,7.,7.])

plt.figure()
plt.plot(t, u, label = "U")
plt.plot(t, v, label = "V")
plt.legend()
plt.savefig("serie.png")
umed = sum(u)/len(u)
vmed = sum(v)/len(v)
cov = 0
for i in range(len(u)):
    cov += ((u[i] - umed)*(v[i] - vmed))/(len(u)-1)
    
print("La covarianza es", cov)
