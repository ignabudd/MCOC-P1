import matplotlib.pylab as plt
from leer_eof import leer_eof
import numpy as np
from satelite import satelite
from scipy.integrate import odeint
from time import perf_counter
from Eulerint import eulerint

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

#Posicion inicial predicha

z0 = np.array([x_i, y_i, z_i, vx_i, vy_i, vz_i]) 

t1 = perf_counter()
sol = odeint(satelite, z0, t) 
t2 = perf_counter()
dt = t2 - t1

sol_ode = sol[:, 0:3] 

delta = np.sqrt((sol[:,0]-x)**2+(sol[:,1]-y)**2+(sol[:,2]-z)**2)
delta_max = round(delta[-1]/1000,2)


#plt.figure()
#plt.plot(t/horas,delta/1000)
#plt.title(f"Distancia entre posicion real y predicha: {delta_max} km")
#plt.xlabel("Tiempo (horas)")
#plt.ylabel("Deriva (Km)")
#plt.savefig("Distancia pos. real y predicha.png", DPI=1200)
#plt.show()


t3 = perf_counter()
sol_euler = eulerint(satelite,z0,t, Nsubdivisiones=1)
t4 = perf_counter()
dt1 = t4 -t3
sol_e = sol_euler[:, 0:3]


Nt = len(t)
Ndim = len(np.array(z0))
z = np.zeros((Nt,Ndim))
z2 = np.zeros((Nt,Ndim))

for i in range(1,Nt):
    
    deriva_ode = np.sqrt(sol_ode[i][0]**2 + sol_ode[i][1]**2 + sol_ode[i][2]**2 )
    deriva_eul = np.sqrt(sol_e[i][0]**2 + sol_e[i][1]**2 + sol_e[i][2]**2)
    z[i,:] = deriva_eul-deriva_ode
    
der_ode_eule = round(z[-1][-1]/1000,2)  

print (f"La deriva entre eulerint (N =1) y odeint es: {der_ode_eule} km")
print (f"La solucion odeint se demora: {dt} segundos")
print (f"La solucion eulerint, Nsubd = 1, se demora: {dt1} segundos")   



plt.figure()
plt.plot(t/horas,z[:]/1000)
plt.title(f"Distancia entre posicion euler y odeint: {der_ode_eule} km")
plt.xlabel("Tiempo (horas)")
plt.ylabel("Deriva (Km)")
plt.savefig("Distancia pos. euler y odeint (N=1).png", DPI=1200)
plt.show()





