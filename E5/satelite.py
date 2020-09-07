# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 21:53:18 2020

@author: ignab
"""

# ---- ORBITA PREDICHA ----

#Unidades Base

G = 6.67*(10**-11)                   #m**3/(kg*s**2)
masa_tierra = 5.972*(10**24)         #kg
omega = 7.27*(10**-5)                #rad/s
horas = 3600 


import numpy as np

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
    
    zp[3:6] = -G*masa_tierra*z1/(r_3) - R.T@  (2*R_prima @ z2 + R_primaprima @ z1)
    
    return zp  



#Unidades Base

G = 6.67*(10**-11)                   #m**3/(kg*s**2)
masa_tierra = 5.972*(10**24)         #kg
omega = 7.27*(10**-5)                #rad/s
horas = 3600 

km = 1000
omega = 7.292115*10**(-5)           #rad/s
km3 = 1000**3
km5 = 1000**5
km6 = 1000**6
mu = 398600.44*km3
J2 = 1.75553e10*km5    #m5
J3 = -2.61913e11*km6   #m5
G = 6.67408e-11        # m3/(kg s2)
mt = 5.972e-24         # kg


def satelite_j2(z,t):
    zp = np.zeros(6)
    R = np.array([[np.cos(omega*t) , -np.sin(omega*t), 0], 
                   [np.sin(omega*t) , np.cos(omega*t), 0 ], 
                   [0               , 0              , 1]])
    R_prima = omega*np.array([[-np.sin(omega*t), -np.cos(omega*t), 0], 
                              [np.cos(omega*t) , -np.sin(omega*t), 0 ], 
                              [0               , 0               , 0]])
    R_primaprima = (omega**2)*np.array([[-np.cos(omega*t) , np.sin(omega*t), 0], 
                                        [-np.sin(omega*t) , -np.cos(omega*t), 0 ], 
                                        [0                , 0               , 0]])
            
    
    x = z[0:3]
    xp = z[3:6]
    r = np.sqrt(np.dot(x,x))
    x_mult = R@x
    rnorma = x_mult/r
    
    Fg = -mu/r**2*rnorma
    
    z2 = x_mult[2]**2
    
    rp = x_mult[0]**2 + x_mult[1]**2
    
    fj2 = J2*x_mult/r**7
    
    fj2[0] = fj2[0]*(6*z2 - (3/2)*rp)
    fj2[1] = fj2[1]*(6*z2 - (3/2)*rp)
    fj2[2] = fj2[2]*(3*z2 - (9/2)*rp)
    
    zp[0:3] = xp
    zp[3:6] = R.T @ (Fg + fj2 - (2*R_prima@xp + R_primaprima@x))
    
    
    
    return zp  

def satelite_j2j3(z,t):
    zp = np.zeros(6)
    R = np.array([[np.cos(omega*t) , -np.sin(omega*t), 0], 
                   [np.sin(omega*t) , np.cos(omega*t), 0 ], 
                   [0               , 0              , 1]])
    R_prima = omega*np.array([[-np.sin(omega*t), -np.cos(omega*t), 0], 
                              [np.cos(omega*t) , -np.sin(omega*t), 0 ], 
                              [0               , 0               , 0]])
    R_primaprima = (omega**2)*np.array([[-np.cos(omega*t) , np.sin(omega*t), 0], 
                                        [-np.sin(omega*t) , -np.cos(omega*t), 0 ], 
                                        [0                , 0               , 0]])
            
    
    x = z[0:3]
    xp = z[3:6]
    r = np.sqrt(np.dot(x,x))
    x_mult = R@x
    rnorma = x_mult/r
    
    Fg = -mu/r**2*rnorma
    
    z2 = x_mult[2]**2
    
    rp = x_mult[0]**2 + x_mult[1]**2
    
    fj2 = J2*x_mult/r**7
    
    fj2[0] = fj2[0]*(6*z2 - (3/2)*rp)
    fj2[1] = fj2[1]*(6*z2 - (3/2)*rp)
    fj2[2] = fj2[2]*(3*z2 - (9/2)*rp)
    
    fj3 = np.zeros(3)
    fj3[0] = J3*x_mult[0]*x_mult[2]/r**9 * (10 * z2 - (15/2)*rp)
    fj3[1] = J3*x_mult[1]*x_mult[2]/r**9 * (10 * z2 - (15/2)*rp)
    fj3[2] = J3/r**9 * (4 * z2 * (z2 - 3*rp) + (3/2)*rp**2)
    
    
    zp[0:3] = xp
    zp[3:6] = R.T @ (Fg + fj2 + fj3 - (2*R_prima@xp + R_primaprima@x))
    
    
    
    return zp  
