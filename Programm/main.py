import numpy as np
import sympy
import matplotlib.pyplot as plt

x,y,z = np.meshgrid(np.linspace(-5,5,20),np.linspace(-5,5,20),np.linspace(-5,5,20))

u = x/np.sqrt(x**2 + y**2 + z**2)
v = y/np.sqrt(x**2 + y**2 + z**2)
k = z/np.sqrt(x**2 + y**2 + z**2)

ax = plt.figure().add_subplot(projection='3d')

ax.quiver(x,y,z,u,v,k,length=0.1, normalize=True)
plt.show()
