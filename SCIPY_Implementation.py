'''
CS 558

Authors: Haval Ahmed(815013661) and Ryan Stevens()

Assignment #2 Simulation #1

How To Run: Click Run and at the end of the simulation, there will be some console information as well
            as graphs to show statistical information.

First Order Equations:
dm/dt = 2m - ams, m(0) = m0
ds/dt = -s + ams, s(0) = s0

Variables For First Order Equation:
T = Time
M = M(t) is the number of mackerel
S = S(t) is the number of shark
A is a positive constant.

'''


import scipy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

