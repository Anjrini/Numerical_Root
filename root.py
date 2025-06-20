# -*- coding: utf-8 -*-
"""
Created on Sun May 18 21:32:46 2025

@author: Mustafa anjrini
"""

import numpy as np

#approximation of the root

def root(x):
    if x<0:
        return("Number below zero! no root exists")
    elif x==0:
        return 0
    else:
        x0=x/10
        while True:
            x1=0.5*(x0+x/x0)
            if np.abs(x1-x0)<1e-4:
                break
            else:
                x0=x1
    return x1

#let's test the function    
root(10)
