# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 10:52:13 2020

@author: ignab
"""
import numpy as np
from numpy import *
from scipy.integrate import odeint
import matplotlib.pylab as plt

pi= np.pi
m = 1                   # Kg
f = 1                   # Hz
chi = 0.2
omega = 2*pi*f
k = m*omega**2
c = 2*chi*omega*m

def eulerint(zp, z0, t, Nsubdivisiones=1):
    Nt = len(t)
    Ndim = len(np.array(z0))
    z = np.zeros((Nt,Ndim))
    z[0,:] = z0
    
    for i in range(1, Nt):
    
        t_anterior = t[i-1]
        
        dt = (t[i] - t[i-1])/Nsubdivisiones
        
        z_temp = z[i-1, :].copy()
        
        for k in range(Nsubdivisiones):
            z_temp += dt*zp(z_temp , t_anterior + k*dt)
            
        z[i,:] = z_temp
        
    return z


def zp(z,t):
    
    zp = np.zeros(2)
    
    zp[0] = z[1]

    zp[1] = -c*z[1]/m - k*z[0]/m
    
    return zp

#Cond iniciales
z0 = [1,1]

t = np.linspace(0, 4, 100)

# Odeint
z_odeint = odeint(zp, z0, t)


# Real  solucion analitica
# Solución encontrada
z_real = np.exp(-chi*omega*t)*(m*cos(omega*((1-chi**2)**0.5)*t) + 
                              ((1 + omega*chi*m)/(omega*((1-chi**2)**0.5)))*sin(omega*((1-chi**2)**0.5)*t))

# Euler
z_euler1 = eulerint(zp,z0,t, Nsubdivisiones=1)
z_euler10 = eulerint(zp, z0, t, Nsubdivisiones=10)
z_euler100 = eulerint(zp, z0, t, Nsubdivisiones=100)

plt.figure()

plt.plot(t,z_real, label="real", color = "black", linewidth = 2)
plt.plot(t,z_odeint[:,0], label="odeint", color= "blue")
plt.plot(t,z_euler1[:,0], linestyle = "--", label="euler N = 1", color ="green")
plt.plot(t,z_euler10[:,0],linestyle = "--", label="euler N = 10", color = "red")
plt.plot(t,z_euler100[:,0], linestyle = "--", label="euler N= 100", color= "orange")


plt.legend()
plt.xlim(0,4)
plt.xlabel("t [seg]")
plt.ylabel("x(t)")
plt.tight_layout()
plt.grid()

plt.savefig(" Entrega 4.png")
plt.show()

