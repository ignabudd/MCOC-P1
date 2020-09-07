# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 21:28:12 2020

@author: ignab
"""

import numpy as np
from leer_eof import leer_eof


def eulerint(zp, zi, t, Nsubdivisiones=1):
    Nt = len(t)
    Ndim = len(np.array(zi))
    z = np.zeros((Nt,Ndim))
    z[0,:] = zi
    
    for i in range(1, Nt):
    
        t_anterior = t[i-1]
        
        dt = (t[i] - t[i-1])/Nsubdivisiones
        
        z_temp = z[i-1, :].copy()
        
        for k in range(Nsubdivisiones):
            z_temp += dt*zp(z_temp , t_anterior + k*dt)
            
        z[i,:] = z_temp
        
    return z


