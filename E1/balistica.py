# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 12:55:04 2020

@author: ignab
"""

import scipy as sp
from scipy.integrate import odeint
import matplotlib.pylab as plt


#Unidades Base

cm = 0.01 #m
inch = 2.54*cm
g = 9.81 #m/s/S


#Coefieciente de arrastre
rho = 1.225 #kg / m**3
cd = 0.47
D = 8.5*inch
r = D/2
A = sp.pi * r**2
CD = 0.5*rho*cd*A

#Masa
m = 15. #kg

#Viento

Vs = [0, 10, 20] #m/s

# Funcion a integrar:
# z es el vector de estado

# z = [x, y, vx, vy]
# dz/dt = bala(z,t)     dz1/dt = z2
#        [ z2      ]
#dz/dt = [         ]  (modelo)
#        [ FD/m - g]

# Vector de estado
# z[0] -> x
# z[1] -> y
# Z[2] -> vx
# Z[3] -> vy



for j in Vs:
  
    def bala(z,t):
        zp = sp.zeros(4)
        zp[0] = z[2]
        zp[1] = z[3]
    
        v = z[2:4] # saca los utimos dos comp
        v[0] = v[0] - j
        v2 = sp.dot(v,v)
        vnorm = sp.sqrt(v2)
        FD = -CD * v2 * (v/vnorm)
        zp[2] = FD[0]/m
        zp[3] = FD[1]/m - g
    
        return zp

 

    Vs = j
    # vector de tiempo
    t = sp.linspace(0, 30, 1001)
    
    #Parte en el origen y tiene vx 2 m/s y vy = 2 m/s
    vi = 100*1000./3600.
    z0 = sp.array([ 0, 0, vi, vi ])
    
    sol = odeint(bala,z0,t)
    
    x = sol[:,0]
    y = sol[:,1]
    
    plt.plot(x, y , label = f"V = {j} m/s")
    
    
plt.figure(1)
plt.ylim(0,50)
plt.xlim(0,150)
plt.grid(True)
plt.ylabel("Y(m)")
plt.xlabel("X(m)")
plt.title("Trayectoria para distintos vientos")
plt.legend()

plt.tight_layout()

plt.savefig("Trayectoria para distintos vientos.png")
 


















