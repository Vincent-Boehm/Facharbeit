import matplotlib as mpl 
import matplotlib.pyplot as plt
import sympy
import numpy as np
import time

x,y,z = np.meshgrid(np.arange(-1,1,0.1),np.arange(-1,1,0.1),np.arange(-1,1,0.8))

a,b,c = sympy.symbols("a b c")

sympy.init_printing(use_unicode=True)

#Base function to describe the field
f_e = -sympy.sin(a) * -sympy.cos(b) + c



#Take the Diffrential to A
u_ = sympy.diff(f_e,a)

k_ = sympy.diff(f_e,b)

v_ = sympy.diff(f_e,c)


# Create lambdified functions
u_func = sympy.lambdify((a, b, c), u_, 'numpy')
k_func = sympy.lambdify((a, b, c), k_, 'numpy')
v_func = sympy.lambdify((a, b, c), v_, 'numpy')


u = u_func(x, y, z)
k = k_func(x, y, z)
v = v_func(x, y, z)

ax = plt.figure().add_subplot(111,projection='3d')

M = np.sqrt(u**2 + v**2 + k**2)


# Get the colormap
cmap = plt.get_cmap('viridis')

qq=plt.quiver(x,y,z,u,v,k,length=0.1,cmap=cmap,normalize=True,)

plt.colorbar(qq, cmap=plt.cm.jet)

#plt.show()

plt.ioff()

plt.savefig("./images/sin7.png")