import matplotlib
import sympy

x, y, z, t = sympy.symbols("x y z t")

func = x**2 + sympy.cos(y)

derivate_x = sympy.diff(x)
derivate_y = sympy.diff(y)


print(final_func)

sympy.plotting.plot3d(final_func)
 