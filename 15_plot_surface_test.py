import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D

# a square mesh with Z = X^2 + Y^2

x = np.linspace(-1,1,100)
y = np.linspace(-1,1,50)

x_mesh, y_mesh = np.meshgrid(x, y, indexing='ij')

z_mesh = x_mesh**2 + y_mesh**2

colors_ref = np.zeros(z_mesh.shape)
for i in range(len(x)):  # z_mesh.shape[0]
    for j in range(len(y)): # z_mesh.shape[1]
        colors_ref[i,j] = np.sqrt(x_mesh[i,j]**2 + 
                y_mesh[i,j]**2)
colors_norm = colors_ref / np.max(colors_ref)

fig = plt.figure(figsize=[8,6])
sub = fig.add_subplot(111, projection='3d')
surf = sub.plot_surface(x_mesh, y_mesh, z_mesh,
    cmap=plt.cm.PuRd, 
    facecolors=plt.cm.PuRd(colors_norm))

cb = fig.colorbar(surf, shrink=0.8, aspect=15,
    label='$\sqrt{x^2  + y^2}$')

cb.set_ticks( [0, 0.5, 1, np.sqrt(2)] / np.sqrt(2))
cb.ax.set_yticklabels(['0','0.5','1',
    r'$\sqrt{2}$'])

sub.set_xlabel(r'$x$')
sub.set_ylabel(r'$y$')
sub.set_zlabel(r'$z$')

sub.set_xticks([-1,-0.5,0,0.5,1])
sub.set_yticks([-1,-0.5,0,0.5,1])
sub.set_zticks([0,0.5,1,1.5,2])


sub.set_title(r'$z=x^2 + y^2$',fontsize=15)

fig.tight_layout()

plt.show()

# fig.savefig('./figure.png',dpi=400)