import matplotlib as mpl 
import matplotlib.pyplot as plt
import sympy
import numpy as np

x,y,z = np.meshgrid(np.linspace(10,-10,20),np.linspace(10,-10,20),np.linspace(10,-10,3))

a,b,c = sympy.symbols("a b c ")

sympy.init_printing(use_unicode=True)

#Base function to describe the field
f_a_x = -1/(a**2 + b**2 + c**2)
f_a_y = -1/(a**2 + b**2 + c**2)
f_a_z = -1/(a**2 + b**2 + c**2)


f_a_x_d = sympy.diff(f_a_x,a)
f_a_y_d = sympy.diff(f_a_y,b)
f_a_z_d = sympy.diff(f_a_z,c)
B = sympy.Matrix([
    f_a_z_d - f_a_y_d,
    f_a_x_d - f_a_z_d,
    f_a_y_d - f_a_x_d
])

print(B)

print(B[0])


f_e_x_func = sympy.lambdify((a, b, c), B[0], 'numpy')

f_e_y_func = sympy.lambdify((a, b, c), B[1], 'numpy')

f_e_z_func = sympy.lambdify((a, b, c), B[2], 'numpy')


#Take the Diffrential to A
u_ = sympy.diff(B[0],c)


k_ = sympy.diff(B[1],b)
v_ = sympy.diff(B[2],a)


J = sympy.Matrix([
    v_ - k_,
    u_ - v_,
    k_ - u_
])

J_x_func = sympy.lambdify((a,b,c), J[0], "numpy")
J_y_func = sympy.lambdify((a,b,c), J[1], "numpy")
J_z_func = sympy.lambdify((a,b,c), J[2], "numpy")

J_X = J_x_func(x,y,z)
J_Y = J_y_func(x,y,z)
J_Z = J_z_func(x,y,z)
print(J)


u_e = f_e_x_func(x,y,z)
k_e = f_e_y_func(x,y,z)
v_e = f_e_z_func(x,y,z)


fig, axs = plt.subplots(2, 1,figsize=(10, 10),subplot_kw={'projection': '3d'})

M1 = np.sqrt(u_e ** 2 + k_e**2)


M2 = np.sqrt(J_X ** 2 + J_Y**2)


# Plot the quiver plot in the first subplot
qq = axs[0].quiver(x,y,z,u_e,k_e,v_e,normalize=True)
axs[0].set_title("Magnetisches Feld") 
cbar_qq = plt.colorbar(qq, ax=axs[0])

#Plot the contour plot in the second subplot
pp = axs[1].quiver(x,y,z,J_X,J_Y,J_Z,normalize=True)
axs[1].set_title('Elektrischer Fluss')
cbar_pp = plt.colorbar(pp, ax=axs[1])

# Adjust layout to prevent overlapping
plt.tight_layout()

plt.ioff()

plt.savefig("./Programm/images/3d_ish/m/123123.png")