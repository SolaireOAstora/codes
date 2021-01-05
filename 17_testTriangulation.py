import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import sys
from matplotlib.patches import Polygon

# x = [0.8, 0.4, 0.5, 0.1, 0.9]
# y = [0.9, 0.2, 0.5, 0.6, 0.1]

# N = len(x)

N = 100
x = np.random.rand(N)
y = np.random.rand(N)

# triangles = [ [2,0,3], [1,2,3] ]
# triangles = [[2,0,3],[1,2,3],[1,0,2],[1,4,0]]

triangulation = mtri.Triangulation(x,y)
# print(triangulation.edges)

# sys.exit()

fig = plt.figure()
sub = fig.add_subplot(111)
# sub.scatter(x,y,marker='o', color='k', s=50)
# for i in range(N):
#     sub.text(x[i]+0.02, y[i]+0.02, 
#         '{:d}'.format(i), fontsize=12)

sub.triplot(triangulation, color='k')


triangles = np.array(triangulation.triangles)
ntri = len(triangles)

# for i in range(ntri):
#     vertices = np.zeros([3,2])
#     # triangles[i,j]: i-th triangle's j-th vertex
#     for j in range(3):
#         vertices[j,0] = x[triangles[i,j]]
#         vertices[j,1] = y[triangles[i,j]]

#     x_center = (x[triangles[i,0]] + 
#         x[triangles[i,1]] + x[triangles[i,2]])/3

#     poly = Polygon(vertices, facecolor=
#         plt.cm.plasma(x_center))
#     sub.add_patch(poly)

sub.set_xlim([0,1])
sub.set_ylim([0,1])
plt.show()