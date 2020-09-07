import matplotlib.pylab as plt
from leer_eof import leer_eof
import numpy as np
from satelite import satelite_j2, satelite_j2j3
from scipy.integrate import odeint
from time import perf_counter

t0 = perf_counter()
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

# Posicion inicial predicha

z0 = np.array([x_i, y_i, z_i, vx_i, vy_i, vz_i]) 


# Con J3
t1 = perf_counter()
sol = odeint(satelite_j2, z0, t) 
t2 = perf_counter()
dt = t2 - t1

sol_ode = sol[:, 0:3] 
sol_ode1 = sol[:, 3:6]


delta = np.sqrt((sol[:,0]- x)**2+(sol[:,1]-y)**2+(sol[:,2]-z)**2)
delta_max = round(delta[-1]/1000,2)


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

plt.savefig("P4 - Posicion XYZ (j2).png", DPI=1200)
plt.show() 

plt.figure()
plt.plot(t/horas,delta/1000)

plt.title(f"Distancia entre posicion real y predicha: {delta_max} km")
plt.xlabel("Tiempo (horas)")
plt.ylabel("Deriva (Km)")
plt.savefig("P4 - Distancia pos. real y predicha con j2.png", DPI=1200)
plt.show()


# Con J2 y J3

t1 = perf_counter()
sol = odeint(satelite_j2j3, z0, t) 
t2 = perf_counter()
dt = t2 - t1

sol_ode = sol[:, 0:3] 
sol_ode1 = sol[:, 3:6]

delta = np.sqrt((sol[:,0]- x)**2+(sol[:,1]-y)**2+(sol[:,2]-z)**2)
delta_max = round(delta[-1]/1000,2)


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
plt.ylabel("Z (KM)")
plt.xlabel("Tiempo (Horas)")
plt.savefig("P4 - Posicion XYZ (j2j3) .png", DPI=1200)
plt.show() 

plt.figure()
plt.plot(t/horas,delta/1000)
plt.title(f"Distancia entre posicion real y predicha: {delta_max} km")
plt.xlabel("Tiempo (horas)")
plt.ylabel("Deriva (Km)")
plt.savefig("P4 - Distancia pos. real y predicha con j2j3.png", DPI=1200)
plt.show()

tf = perf_counter()
dtc = tf - t0
print (f"El codigo se demora {dtc} s en correr.")






































