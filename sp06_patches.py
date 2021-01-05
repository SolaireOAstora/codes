import matplotlib.pyplot as plt 
from matplotlib.patches import *
from numpy import pi

# # # Circle
# patch = Circle((0.5,0.5), 0.5,
#     edgecolor='k', facecolor='C1',
#     linewidth=2, linestyle='--',
#     hatch='X')

# # Ellipse
# patch = Ellipse(xy=(0.5,0.5), width=1, height=0.5,
#     edgecolor='C0', facecolor='C1', angle=30)

# # Arc
# patch = Arc(xy=(0.5,0.5), width=0.5, height=0.5,
#     edgecolor = 'C0', lw=2, theta1=0, theta2=180,
#     angle=30)

# Wedge
patch = Wedge(center=(0.5, 0.5), r=0.5,
    theta1=0, theta2=360, facecolor='C2',
    edgecolor='k', lw=2, width=0.1)

# shadow
shadow = Shadow(patch, ox=-0.01, oy=0.02,
    props=dict(facecolor='yellow',
        edgecolor='red',alpha=0.4))

# # Circlepolygon
# patch = CirclePolygon(xy=(0.5,0.5), radius=0.5,
#     resolution=20)

# # Rectangle
# patch = Rectangle(xy=(0.5,0.5), width=1, height=0.5,
#     angle=30)

# # RegularPolygon
# patch = RegularPolygon(xy=(0.5,0.5),
#     numVertices=6, radius=0.5,
#     orientation=pi/6)


# plot
fig = plt.figure()
sub = fig.add_subplot(111)
sub.add_patch(patch)
sub.add_patch(shadow)
sub.set_aspect('equal')
sub.set_xlim([0,1])
sub.set_ylim([0,1])

sub.spines['left'].set_visible(False)
sub.spines['right'].set_visible(False)
sub.spines['bottom'].set_visible(False)
sub.spines['top'].set_visible(False)

# sub.axes.xaxis.set_visible(False)
# sub.axes.yaxis.set_visible(False)

sub.xaxis.set_visible(False)
sub.yaxis.set_visible(False)

plt.show()