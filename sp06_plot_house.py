import matplotlib.pyplot as plt 
from matplotlib.patches import *
import numpy as np 

body = Rectangle(xy=[0.25,0], width=1,
    height=1, facecolor='green', edgecolor='k')

center = 1 + 0.5 * np.tan(np.pi/6)
roof = CirclePolygon(xy=[0.75, center],
    radius = 0.5 / np.cos(np.pi/6), resolution=3,
    facecolor='brown', edgecolor='k')

door = Rectangle(xy=[0.8,0], width=0.3,
    height=0.5, edgecolor='k', facecolor='blue')

knob = Circle(xy=[0.9,0.25], radius=0.05, 
    edgecolor='k', facecolor='green')

sun = Circle(xy=[2.5,1.5], radius=0.3, 
    color='gold')

fig = plt.figure(figsize=[7,5], facecolor=
    'lightsteelblue')
sub=fig.add_subplot(111,facecolor=
    'lightsteelblue')
sub.add_patch(body)
sub.add_patch(roof)
sub.add_patch(door)
sub.add_patch(knob)
sub.add_patch(sun)
sub.set_aspect('equal')

sub.set_xlim([0,3])
sub.set_ylim([0,2])

sub.spines['left'].set_visible(False)
sub.spines['right'].set_visible(False)
sub.spines['bottom'].set_visible(False)
sub.spines['top'].set_visible(False)

sub.axes.xaxis.set_visible(False)
sub.axes.yaxis.set_visible(False)


plt.show()
# fig.savefig('./figure.png', facecolor=
#     'lightsteelblue')