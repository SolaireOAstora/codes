import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.tri import Triangulation
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

N = 200
r = np.random.rand(N)
theta = np.random.rand(N) * 2 * np.pi 

x = r * np.cos(theta)
y = r * np.sin(theta)

# fig = plt.figure()
# sub = fig.add_subplot(111, aspect='equal')
# sub.scatter(x,y,s=10)
# plt.show()

z = np.sqrt(1-x**2-y**2)

# fig = plt.figure()
# sub = fig.add_subplot(111, projection='3d')
# # sub.scatter(x,y,z,s=10)
# sub.plot_trisurf(x,y,z, cmap='rainbow')
# plt.show()


triang = Triangulation(x,y)
triangles = triang.triangles
ntri = triangles.shape[0]


# mask = np.zeros(ntri, dtype=bool)
# for i in range(ntri):
#     if np.min(r[triangles[i]])<=0.4:
#         mask[i] = True
# triang.set_mask(mask)

# fig = plt.figure()
# sub = fig.add_subplot(111, projection='3d')
# sub.plot_trisurf(triang,z, cmap='rainbow')
# plt.show()

vertices = np.zeros([ntri,3,3])
colors_ref = np.zeros(ntri)
for i in range(ntri):
    for j in range(3):
        index = triangles[i,j]
        vertices[i,j,0] = x[index]
        vertices[i,j,1] = y[index]
        vertices[i,j,2] = z[index]

    colors_ref[i] = (np.mean(x[triangles[i]]) + 1)/2


colors_ref = np.random.rand(ntri)
coll = Poly3DCollection(vertices, edgecolors='k',
    linewidth=0.3, facecolors=plt.cm.rainbow(colors_ref))

fig = plt.figure()
sub = fig.add_subplot(111,projection='3d')
sub.add_collection(coll)
sub.set_xlim([-1,1])
sub.set_ylim([-1,1])
sub.set_zlim([0,1])
sub.set_xlabel(r'$x$', fontsize=14)
sub.set_ylabel(r'$y$', fontsize=14)
sub.set_zlabel(r'$z$', fontsize=14)
plt.show()