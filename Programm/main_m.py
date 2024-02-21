import matplotlib as mpl 
import matplotlib.pyplot as plt
import sympy
import numpy as np
import time

x,y,z = np.meshgrid(np.arange(-2,2,0.1),np.arange(-2,2,0.1),np.arange(-2,2,0.1))

a,b,c = sympy.symbols("a b c")

sympy.init_printing(use_unicode=True)

#Base function to describe the field
f_e = a/sympy.sqrt(a**2 + b**2 + c**2) - b/sympy.sqrt(b**2 + a**2 + c** 2) - c/sympy.sqrt(c**2 + a**2 + b**2)
f_e_func = sympy.lambdify((a, b, c), f_e, 'numpy')


#Take the Diffrential to A
u_ = sympy.diff(f_e,a)
k_ = sympy.diff(f_e,b)
v_ = sympy.diff(f_e,c)

J = sympy.Matrix([
    v_ - k_,
    u_ - v_,
    k_ - u_
])

print(J)

# Create lambdified functions
u_func = sympy.lambdify((a,b,c), J[0], 'numpy')
k_func = sympy.lambdify((a,b,c), J[1], 'numpy')
v_func = sympy.lambdify((a,b,c), J[2], "numpy")

u = u_func(x,y,z)
k = k_func(x,y,z)
v = v_func(x,y,z)


print(x.shape)


fig, axs = plt.subplots(2, 1,figsize=(10, 10))

M = np.sqrt(u[:,:,0]**2  + k[:,:,0]**2)



# Plot the quiver plot in the first subplot
qq = axs[0].quiver(x[:,:,0], y[:,:,0], u[:,:,0], k[:,:,0], M, cmap=plt.cm.jet)
axs[0].set_title("Elektrischer Fluss") 
cbar_qq = plt.colorbar(qq, ax=axs[0])

# Plot the contour plot in the second subplot
pp = axs[1].quiver(x[:,:,0], y[:,:,0], f_e_func(x, y, z)[:,:,0], cmap=plt.cm.jet)
axs[1].set_title('Magnetische Feldstärke ')
cbar_pp = plt.colorbar(pp, ax=axs[1])

# Adjust layout to prevent overlapping
plt.tight_layout()

#plt.show()

plt.ioff()

plt.savefig("./Programm/images/testtest.png")