import matplotlib as mpl 
import matplotlib.pyplot as plt
import sympy
import numpy as np
import time

x,y,z = np.meshgrid(np.linspace(-1,1,0.2),np.linspace(-1,1,0.2),np.linspace(-1,1,0.2))

a,b,c = sympy.symbols("a b c")

sympy.init_printing(use_unicode=True)

#Base function to describe the field
f_e = 1/(a**2 + b**2 + c**2)


#Take the Diffrential to A
u = sympy.diff(f_e,a)

k = sympy.diff(f_e,b)

v = sympy.diff(f_e,c)


ax = plt.figure().add_subplot(projection='3d')


qq=plt.quiver(x,y,z,u,v,k,cmap=plt.cm.jet)

plt.colorbar(qq, cmap=plt.cm.jet)

plt.show()

#plt.ioff()

#plt.savefig("05.02.2024.png")