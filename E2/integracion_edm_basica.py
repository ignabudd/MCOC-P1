# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:09:58 2020

@author: ignab
"""

import scipy as sp
import numpy as np
from scipy.integrate import odeint
import matplotlib.pylab as plt

#Unidades Base

G = 6.67*(10**-11)*(1*10**-9)*(3600**2) #km**3/(kg*h**2)
radio_tierra = 6371 #km
masa_tierra = 5.972*(10**24) #kg
omega = 7.27*(10**-5)/(1/3600) #rad/h
alt_sat = 700 #km



def satelite(z,t):
    
    R = np.array([[np.cos(omega*t) , -np.sin(omega*t), 0], 
                   [np.sin(omega*t) , np.cos(omega*t), 0 ], 
                   [0               , 0              , 1]])
    R_prima = omega*np.array([[-np.sin(omega*t), -np.cos(omega*t), 0], 
                              [np.cos(omega*t) , -np.sin(omega*t), 0 ], 
                              [0               , 0               , 0]])
    R_primaprima = (omega**2)*np.array([[-np.cos(omega*t) , np.sin(omega*t), 0], 
                                        [-np.sin(omega*t) , -np.cos(omega*t), 0 ], 
                                        [0                , 0               , 0]])
            
    
    zp = np.zeros(6)
    
    zp[0] = z[3]
    zp[1] = z[4]
    zp[2] = z[5]
    
    r_3 = (np.sqrt(z[0]**2 + z[1]**2 + z[2]**2))**3 
    
    z1 = z[0:3]
    z2 = z[3:6]
    
    zp[3:6] = -G*masa_tierra*z1/(r_3) - R.T @ (2*R_prima @ z2 + R_primaprima @ z1)
    
    return zp 


# Vector de tiempo en segundos
h = 3.5 #horas
t = np.linspace(0,h,10000)

#Yo establezco una vi = X km/h

vi = 24550 #km/h

z0 = np.array([radio_tierra+alt_sat, 0, 0, 0, vi, 0])

sol = odeint(satelite, z0, t)


plt.figure(1)

x = sol[:,0]
y = sol[:,1]
z = sol[:,2]


plt.subplot(3,1,1)
plt.title("Historias de tiempo")
plt.plot(t,x)
plt.ylabel("Km")
plt.xlabel("X(t)")
plt.xlim(0,h)
plt.grid()


plt.subplot(3,1,2)
plt.plot(t,y)
plt.ylabel("Km")
plt.xlabel("Y(t)")
plt.xlim(0,h)
plt.grid()

plt.subplot(3,1,3)
plt.plot(t,z)
plt.ylabel("Km")
plt.xlabel("X(t)")
plt.xlim(0,h)
plt.grid()

plt.xlabel("Tiempo transcurrido (horas)")
plt.legend()
plt.tight_layout()

plt.savefig("Hitsorias de tiempo.png")
 
plt.figure(2) 

d = 80 #km
r = np.sqrt((x**2+y**2+z**2))

plt.plot(t,r)
plt.xlim(0,h)
plt.grid()
plt.tight_layout()
plt.hlines(radio_tierra+d, 0, h, color = 'dodgerblue')
plt.ylabel("r(t) [km]")
plt.xlabel("t [h]")

plt.savefig("Trayectoria Satelite Vista 1.png")


plt.figure(3)

rad = radio_tierra+d 
plt.figure(3)
angulo = np.linspace(0, 2*np.pi, 1000)
x1 = rad * np.cos(angulo)
y1 = rad * np.sin(angulo)
plt.axis("equal")
plt.title("Trayectoria Satélite")
plt.plot(x1,y1, color = "g", label = "Tierra")
plt.plot(x,y, label = "Satélite")
plt.ylabel("Km")
plt.xlabel("Km")
plt.tight_layout()
plt.legend()
plt.grid()

plt.savefig("Trayectoria Satelite Vista 2.png")

plt.show()












