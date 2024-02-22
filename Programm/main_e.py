import matplotlib as mpl 
import matplotlib.pyplot as plt
import sympy
import numpy as np

x,y,z = np.meshgrid(np.linspace(10,-10,20),np.linspace(10,-10,20),np.linspace(10,-10,20))

a,b,c = sympy.symbols("a b c ")

sympy.init_printing(use_unicode=True)

#Base function to describe the field
f_e_x = 1/(1+sympy.E ** -a) + b
f_e_y = 1/(1+sympy.E ** -b) + a

f_e_z = c**2


f_e_x_func = sympy.lambdify((a, b, c), f_e_x, 'numpy')

f_e_y_func = sympy.lambdify((a, b, c), f_e_y, 'numpy')

f_e_z_func = sympy.lambdify((a, b, c), f_e_z, 'numpy')


#Take the Diffrential to A
u_ = sympy.diff(f_e_x,a)
k_ = sympy.diff(f_e_y,b)
v_ = sympy.diff(f_e_z,c)



# Create lambdified functions
u_func = sympy.lambdify((a,b,c), u_, 'numpy')
k_func = sympy.lambdify((a,b,c), k_, 'numpy')
v_func = sympy.lambdify((a,b,c), v_, "numpy")


u_e = f_e_x_func(x,y,z)
k_e = f_e_y_func(x,y,z)
v_e = f_e_z_func(x,y,z)

u_c = u_func(x,y,z)
k_c = k_func(x,y,z)
v_c = v_func(x,y,z)


s = u_c + k_c + v_c

print(s)

fig, axs = plt.subplots(2, 1,figsize=(10, 10))

M = np.sqrt(u_e[:,:,0] ** 2 + k_e[:,:,0]**2)


# Plot the quiver plot in the first subplot
qq = axs[0].quiver(x[:,:,0],y[:,:,0],u_e[:,:,0],k_e[:,:,0], M, cmap=plt.cm.jet)
axs[0].set_title("Elektrisches Feld") 
cbar_qq = plt.colorbar(qq, ax=axs[0])

#Plot the contour plot in the second subplot
pp = axs[1].contourf(x[:,:,0],y[:,:,0],s[:,:,0], cmap=plt.cm.jet, levels=100)
axs[1].set_title('Elektrische Ladungsdichte')
cbar_pp = plt.colorbar(pp, ax=axs[1])

# Adjust layout to prevent overlapping
plt.tight_layout()

plt.ioff()

plt.savefig("./Programm/images/3d_ish/e/123123.png")