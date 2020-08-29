# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 18:07:42 2020

@author: ignab
"""

import datetime as dt
import numpy as np
from scipy.integrate import odeint


#Unidades Base

G = 6.67*(10**-11)                   #m**3/(kg*s**2)
masa_tierra = 5.972*(10**24)         #kg
omega = 7.27*(10**-5)                #rad/s



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

'''
    <OSV>
      <TAI>TAI=2020-08-04T23:00:19.000000</TAI>
      <UTC>UTC=2020-08-04T22:59:42.000000</UTC>
      <UT1>UT1=2020-08-04T22:59:41.795503</UT1>
      <Absolute_Orbit>+22780</Absolute_Orbit>
      <X unit="m">1586124.423134</X>
      <Y unit="m">-6710400.231480</Y>
      <Z unit="m">1584198.354068</Z>
      <VX unit="m/s">-1940.396189</VX>
      <VY unit="m/s">1260.568183</VY>
      <VZ unit="m/s">7236.973480</VZ>
      <Quality>NOMINAL</Quality>
    </OSV>
'''

'''
    <OSV>
      <TAI>TAI=2020-08-06T01:00:19.000000</TAI>
      <UTC>UTC=2020-08-06T00:59:42.000000</UTC>
      <UT1>UT1=2020-08-06T00:59:41.796128</UT1>
      <Absolute_Orbit>+22795</Absolute_Orbit>
      <X unit="m">-82857.977186</X>
      <Y unit="m">-3709146.708692</Y>
      <Z unit="m">-6032351.101395</Z>
      <VX unit="m/s">-2443.176767</VX>
      <VY unit="m/s">-6089.325952</VY>
      <VZ unit="m/s">3779.934595</VZ>
      <Quality>NOMINAL</Quality>
    </OSV>
    
'''


utc_EOF_format = "%Y-%m-%dT%H:%M:%S.%f"
t1 = dt.datetime.strptime("2020-08-04T22:59:42.000000", utc_EOF_format)
t2 = dt.datetime.strptime("2020-08-06T00:59:42.000000", utc_EOF_format)

delta = t2 - t1
delta_en_seg = delta.total_seconds() #Esto me tira 93600 seg, no se por qué si debiesen ser 7200 seg



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


# Vector de tiempo

t = np.linspace(0,delta_en_seg,93600)

#Pposicion inicial

z0 = np.array([x_i, y_i, z_i, vx_i, vy_i, vz_i]) 

sol = odeint(satelite, z0, t)

x = sol[:, 0:3]

zf =  np.array([x_f, y_f, z_f, vx_f, vy_f, vz_f])

pos_final = zf - sol[-1]


deriva = np.sqrt(pos_final[0]**2 + pos_final[1]**2 + pos_final[2]**2 )

print (f"Diferencia posicion predicha y real: {deriva} [metros] ")


























