# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

sigma = 10
beta = 2.67
rho = 28.0
tfinal = 5.0
N = 1000
dt = tfinal/1000
t = np.zeros(N)
x = np.zeros(N)
y = np.zeros(N)
z = np.zeros(N)
x[0] = 1.0
y[0] = 1.0
z[0] = 1.0
for i in range(1,N):
    x[i] = (sigma*(y[i-1] - x[i-1]))*dt + x[i-1]
    y[i] = ((rho*x[i-1]) - y[i-1] -(x[i-1]*z[i-1]))*dt + y[i-1]
    z[i] = ((-1*beta * z[i-1]) + (x[i-1]*y[i-1]))*dt + z[i-1]

plt.figure()
plt.plot(x, y, label = "X vs Y")
plt.legend()
plt.savefig("xy.png")
plt.figure()
plt.plot(x, z, label = "X vs Z")
plt.legend()
plt.savefig("xz.png")
    







