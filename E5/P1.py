
import matplotlib.pylab as plt
from leer_eof import leer_eof
import numpy as np
from Eulerint import eulerint
from satelite import satelite
from scipy.integrate import odeint
from time import perf_counter

horas = 3600

x_i = 1586124.423134
y_i = -6710400.231480
z_i = 1584198.354068

vx_i = -1940.396189
vy_i = 1260.568183
vz_i = 7236.973480

x_f = -82857.977186
y_f = -3709146.708692
z_f = -6032351.101395

vx_f = -2443.176767
vy_f = -6089.325952
vz_f = 3779.934595

# --- ORBITA REAL ---

t, x, y, z, vx, vy, vz = leer_eof("S1B_OPER_AUX_POEORB_OPOD_20200825T111216_V20200804T225942_20200806T005942.EOF")

#Posicion inicial predicha

z0 = np.array([x_i, y_i, z_i, vx_i, vy_i, vz_i]) 

t1 = perf_counter()
sol = odeint(satelite, z0, t) 
t2 = perf_counter()

dt = t2 - t1


plt.figure(figsize=(19.2,10.8))
plt.subplot(3,1,1)
plt.title("Posición")
plt.plot(t/horas,sol[:,0]/1000)
plt.plot(t/horas,x/1000)
plt.ylabel("X (KM)")

plt.subplot(3,1,2)
plt.plot(t/horas,sol[:,1]/1000)
plt.plot(t/horas,y/1000)
#plt.yticks(ytcks, ytcks)
plt.ylabel("Y (KM)")

plt.subplot(3,1,3)
plt.plot(t/horas,sol[:,2]/1000)
plt.plot(t/horas,z/1000)
#plt.yticks(ytcks, ytcks)
plt.ylabel("Z (KM)")
plt.xlabel("Tiempo (Horas)")

plt.savefig("P1 - Posicion XYZ.png", DPI=1200)
plt.show() 



