import matplotlib as mpl 
import matplotlib.pyplot as plt
from numpy import arange,meshgrid,sqrt
import sympy

import time

x,y,z = arange(-10,10),arange(-10,10)



qq=plt.quiver(x,y,u,v,M,cmap=plt.cm.jet)

plt.colorbar(qq, cmap=plt.cm.jet)

plt.ioff()

plt.savefig("05.02.2024.png")