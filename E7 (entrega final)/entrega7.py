# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 18:24:43 2020

@author: ignab
"""

from leer_eof import leer_eof
import numpy as np
from numpy import sqrt
from scipy.integrate import odeint
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import datetime as dt
from sys import argv

#Unidades Base

G = 6.67*(10**-11)                   #m**3/(kg*s**2)
masa_tierra = 5.972*(10**24)         #kg
horas = 3600 
R = 6378136.3
km = 1000
omega = 7.292115*10**-5              #rad/s
km3 = 1000**3
km5 = 1000**5
km6 = 1000**6
mu = 398600.44*km3


Nt = 8

C = np.zeros((Nt+1,Nt+1))
S = np.zeros((Nt+1,Nt+1)) 

C[4,0], S[4,0] =    0.16193312050719E-05   ,     0.0
C[5,0], S[5,0] =    0.22771610163688E-06   ,     0.0
C[6,0], S[6,0] =   -0.53964849049834E-06   ,     0.0


J2 = 1.75553e10*km5    #m5
J3 = -2.61913e11*km6   #m5
J4 = C[4,0]/((R**4)*mu)
J5 = C[5,0]/((R**5)*mu)
J6 = C[6,0]/((R**6)*mu)


def satelite_j(z,t):
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
    rp2 = x_mult[0]**2 + x_mult[1]**2 + x_mult[2]**2 
    
    fj2 = J2*x_mult/r**7
    
    fj2[0] = fj2[0]*(6*z2 - (3/2)*rp)
    fj2[1] = fj2[1]*(6*z2 - (3/2)*rp)
    fj2[2] = fj2[2]*(3*z2 - (9/2)*rp)
    
    fj3 = np.zeros(3)
    fj3[0] = J3*x_mult[0]*x_mult[2]/r**9 * (10 * z2 - (15/2)*rp)
    fj3[1] = J3*x_mult[1]*x_mult[2]/r**9 * (10 * z2 - (15/2)*rp)
    fj3[2] = J3/r**9 * (4 * z2 * (z2 - 3*rp) + (3/2)*rp**2)
    
    fj4 = np.zeros(3)
    fj4[0] = -5*x_mult[0]*(35*z2**2/((8*rp**2)**2) - 15*x_mult[2]**2/(4*(rp2)) + 0.375)/(rp2)**(7/2) + (-35*x_mult[0]*x_mult[2]**4/(2*(rp2)**3) + 15*x_mult[0]*x_mult[2]**2/(2*(rp2)**2))/(rp2)**(5/2)
    fj4[1] = -5*x_mult[1]*(35*z2**2/((8*rp**2)**2) - 15*x_mult[2]**2/(4*(rp2)) + 0.375)/(rp2)**(7/2) + (-35*x_mult[1]*x_mult[2]**4/(2*(rp2)**3) + 15*x_mult[1]*x_mult[2]**2/(2*(rp2)**2))/(rp2)**(5/2) 
    fj4[2] = -5*x_mult[2]*(35*z2**2/((8*rp**2)**2) - 15*x_mult[2]**2/(4*(rp2)) + 0.375)/(rp2)**(7/2) + (-35*x_mult[2]**5/(2*(rp2)**3) + 25*x_mult[2]**3/((rp2)**2) - 15*x_mult[2]/(2*rp2))/(rp2)**(5/2)
    
    fjn4 = fj4*J4 

    fj5 = np.zeros(3)
    fj5[0] = -6*x_mult[0]*(63*x_mult[2]**5/(8*(rp2)**(5/2)) - 35*x_mult[2]**3/(4*(x_mult[0]**2 + x_mult[1]**2 + x_mult[2]**2)**(3/2)) + 15*x_mult[2]/(8*sqrt(rp2)))/(x_mult[0]**2 + x_mult[1]**2 + x_mult[2]**2)**4 + (-315*x_mult[0]*x_mult[2]**5/(8*(rp2)**(7/2)) + 105*x_mult[0]*x_mult[2]**3/(4*(rp2)**(5/2)) - 15*x_mult[0]*x_mult[2]/(8*(rp2)**(3/2)))/(rp2)**3
    fj5[1] = -6*x_mult[1]*(63*x_mult[2]**5/(8*(rp2)**(5/2)) - 35*x_mult[2]**3/(4*(x_mult[0]**2 + x_mult[1]**2 + x_mult[2]**2)**(3/2)) + 15*x_mult[2]/(8*sqrt(rp2)))/(x_mult[0]**2 + x_mult[1]**2 + x_mult[2]**2)**4 + (-315*x_mult[1]*x_mult[2]**5/(8*(rp2)**(7/2)) + 105*x_mult[1]*x_mult[2]**3/(4*(rp2)**(5/2)) - 15*x_mult[1]*x_mult[2]/(8*(rp2)**(3/2)))/(rp2)**3
    fj5[2] = -6*x_mult[2]*(63*x_mult[2]**5/(8*(rp2)**(5/2)) - 35*x_mult[2]**3/(4*(x_mult[0]**2 + x_mult[1]**2 + x_mult[2]**2)**(3/2)) + 15*x_mult[2]/(8*sqrt(rp2)))/(x_mult[0]**2 + x_mult[1]**2 + x_mult[2]**2)**4 + (-315*x_mult[2]**6/(8*(rp2)**(7/2)) + 525*x_mult[2]**4/(8*(rp2)**(5/2)) - 225*x_mult[2]**2/(8*(rp2)**(3/2)) + 15/(8*sqrt(rp2)))/(rp2)**3
  
    fjn5 = fj5*J5
    
    zp[0:3] = xp
    zp[3:6] = R.T @ (Fg + fj2 + fj3 + fjn4 + fjn5 - (2*R_prima@xp + R_primaprima@x))
    
    
    return zp  

def utc2time(utc, ut1, EOF_datetime_format = "%Y-%m-%dT%H:%M:%S.%f"):
	t1 = dt.datetime.strptime(ut1,EOF_datetime_format)
	t2 = dt.datetime.strptime(utc,EOF_datetime_format)
	return (t2 - t1).total_seconds()


def leer_eof(fname):
	tree = ET.parse(fname)
	root = tree.getroot()

	Data_Block = root.find("Data_Block")		
	List_of_OSVs = Data_Block.find("List_of_OSVs")

	count = int(List_of_OSVs.attrib["count"])
    
	t = np.zeros(count)
	x = np.zeros(count)
	y = np.zeros(count)
	z = np.zeros(count)
	vx = np.zeros(count)
	vy = np.zeros(count)
	vz = np.zeros(count) 
    
	u = []
	for i in range(count):
		u.append([])
    
	set_ut1 = False
	for i, osv in enumerate(List_of_OSVs):
		UTC = osv.find("UTC").text[4:]
		u[i] = osv.find("UTC").text[4:]
		x[i] = osv.find("X").text   #conversion de string a double es implicita
		y[i] = osv.find("Y").text
		z[i] = osv.find("Z").text
		vx[i] = osv.find("VX").text
		vy[i] = osv.find("VY").text
		vz[i] = osv.find("VZ").text

		if not set_ut1:
			ut1 = UTC
			set_ut1 = True

		t[i] = utc2time(UTC, ut1)

	return t, x, y, z, vx, vy, vz, u


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

nombre_eof = argv[1]
#nombre_eof = "S1B_OPER_AUX_POEORB_OPOD_20200825T111216_V20200804T225942_20200806T005942.EOF"
t, x, y, z, vx, vy, vz, u = leer_eof(nombre_eof)

z0 = np.array([x_i, y_i, z_i, vx_i, vy_i, vz_i]) 

sol = odeint(satelite_j, z0, t) 

sol_x = sol[:, 0] 
sol_y = sol[:, 1]
sol_z = sol[:, 2]
sol_vx = sol[:, 3]
sol_vy = sol[:, 4]
sol_vz = sol[:, 5]

eof_out = nombre_eof.replace(".EOF", ".PRED")

EOF_datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
UTC1 = dt.datetime.strptime(u[0],EOF_datetime_format)

with open(eof_out,"w") as fout:
    Nt = len(t)
    fout.write("<Data_Block type=\"xml\">\n  <List_of_OSVs count=\"9361\">\n")
    for i in range(Nt):
        obj = UTC1
        fecha = (obj + timedelta(seconds=t[i])).strftime("%Y-%m-%dT%H:%M:%S.%f")
        fout.write(f"    <OSV>\n      <UTC>UTC={fecha}</UTC>\n      <X unit=\"m\">{sol_x[i]}</X>\n      <Y unit=\"m\">{sol_y[i]}</Y>\n      <Z unit=\"m\">{sol_z[i]}</Z>\n      <VX unit=\"m/s\">{sol_vx[i]}</VX>\n      <VY unit=\"m/s\">{sol_vy[i]}</VY>\n      <VZ unit=\"m/s\">{sol_vz[i]}</VZ>\n      <Quality>NOMINAL</Quality>\n    </OSV>\n")
    fout.write("  </List_of_OSVs>\n</Data_Block>\n</Earth_Explorer_File>")
    
    
delta = np.sqrt((sol[:,0]- x)**2+(sol[:,1]-y)**2+(sol[:,2]-z)**2)
delta_max = round(delta[-1]/1000,2)

print (delta_max)



