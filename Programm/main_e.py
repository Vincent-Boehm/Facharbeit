import matplotlib as mpl 
import matplotlib.pyplot as plt
import sympy
import numpy as np

x,y,z = np.meshgrid(np.arange(-1,1,0.1),np.arange(-1,1,0.1),np.arange(-1,1,0.1))

a,b,c = sympy.symbols("a b c ")

sympy.init_printing(use_unicode=True)

#Base function to describe the field
f_e = a+b+c/sympy.sqrt(a**2 + b**2 + c**2)
f_e_func = sympy.lambdify((a, b, c), f_e, 'numpy')


#Take the Diffrential to A
u_ = sympy.diff(f_e,a)
k_ = sympy.diff(f_e,b)
v_ = sympy.diff(f_e,c)



# Create lambdified functions
u_func = sympy.lambdify((a,b,c), u_, 'numpy')
k_func = sympy.lambdify((a,b,c), k_, 'numpy')
v_func = sympy.lambdify((a,b,c), v_, "numpy")


u = x
k = y
v = z

print(u.shape)

print(x.shape)


fig, axs = plt.subplots(2, 1,figsize=(10, 10))

M = np.sqrt(u[:,:,0]**2  + k[:,:,0]**2)



# Plot the quiver plot in the first subplot
qq = axs[0].quiver(x[:,:,0], y[:,:,0], u[:,:,0], k[:,:,0], M, cmap=plt.cm.jet)
axs[0].set_title("Elektrische Flussdichte") 
cbar_qq = plt.colorbar(qq, ax=axs[0])

# Plot the contour plot in the second subplot
pp = axs[1].contourf(x[:,:,0], y[:,:,0], f_e_func(x, y, z)[:,:,0], cmap=plt.cm.jet, levels=100)
axs[1].set_title('Elektrische Ladungsdichte')
cbar_pp = plt.colorbar(pp, ax=axs[1])

# Adjust layout to prevent overlapping
plt.tight_layout()

plt.ioff()

plt.savefig("./Programm/images/3d_ish/e/test.png")