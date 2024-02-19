import matplotlib as mpl 
import matplotlib.pyplot as plt
import sympy
import numpy as np
import time

x,y, = np.meshgrid(np.arange(-1,1,0.1),np.arange(-1,1,0.1))

a,b, = sympy.symbols("a b")

sympy.init_printing(use_unicode=True)

#Base function to describe the field
f_e = -sympy.sin(a) * -sympy.cos(b)
f_e_func = sympy.lambdify((a, b), f_e, 'numpy')


#Take the Diffrential to A
u_ = sympy.diff(f_e,a)

k_ = sympy.diff(f_e,b)



# Create lambdified functions
u_func = sympy.lambdify((a, b), u_, 'numpy')
k_func = sympy.lambdify((a, b), k_, 'numpy')


u = u_func(x, y)
k = k_func(x, y)

fig, axs = plt.subplots(2, 1,figsize=(10, 10))

M = np.sqrt(u**2  + k**2)



# Plot the quiver plot in the first subplot
qq = axs[0].quiver(x, y, u, k, M, cmap=plt.cm.jet)
axs[0].set_title("elektrische Flussdichte") 
cbar_qq = plt.colorbar(qq, ax=axs[0])

# Plot the contour plot in the second subplot
pp = axs[1].contourf(x, y, f_e_func(x, y), cmap=plt.cm.jet, levels=100)
axs[1].set_title('elektrische Ladungsdichte')
cbar_pp = plt.colorbar(pp, ax=axs[1])

# Adjust layout to prevent overlapping
plt.tight_layout()

#plt.show()

plt.ioff()

plt.savefig("./Programm/images/1.png")