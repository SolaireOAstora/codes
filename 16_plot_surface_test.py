import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D

R = 1.0 
R0 = 0.01 

nrad = 50 
radius = np.concatenate([np.linspace(R0,R,nrad),
    np.linspace(R,R0,nrad)])

phi = np.linspace(0,2*np.pi, 100)

r_mesh, phi_mesh = np.meshgrid(radius, phi, 
    indexing='ij')


x_mesh = r_mesh * np.cos(phi_mesh)
y_mesh = r_mesh * np.sin(phi_mesh)

# plt.scatter(x_mesh.flatten(), y_mesh.flatten(),
#     s=1)
# plt.show()


z_mesh = np.zeros(r_mesh.shape)
for i in range(r_mesh.shape[0]):
    for j in range(r_mesh.shape[1]):
        if i<nrad:
            z_mesh[i,j] = np.sqrt(R**2 - 
                r_mesh[i,j]**2)
        else:
            z_mesh[i,j] = -np.sqrt(R**2 - 
                r_mesh[i,j]**2)


fig = plt.figure()
sub = fig.add_subplot(111, projection='3d')

colors_ref = np.zeros(r_mesh.shape)
for i in range(r_mesh.shape[0]):
    for j in range(r_mesh.shape[1]):
        colors_ref[i,j] = phi_mesh[i,j]
        # colors_ref[i,j] = r_mesh[i,j]/R

colors = colors_ref / np.max(colors_ref)

sub.plot_surface(x_mesh, y_mesh, z_mesh, 
    facecolors=plt.cm.hsv(colors), 
    cmap=plt.cm.hsv)

sub.set_xlabel(r'$x$', fontsize=14)
sub.set_ylabel(r'$y$', fontsize=14)
sub.set_zlabel(r'$z$', fontsize=14)

plt.show()