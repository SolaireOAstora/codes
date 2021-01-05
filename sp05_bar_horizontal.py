import numpy as np 
import matplotlib.pyplot as plt 

names = ['Zhang', 'Wang', 'Li']
values = [10, 6, 15]
values2 = [5,8,3]
height = 0.4

y = np.array([0,1,2])

fig = plt.figure()
sub = fig.add_subplot(111)
sub.barh(y=y-height/2, width=values, height=height,
    color='C0')
sub.barh(y=y+height/2, width=values2,
    height=height, color='C1')

sub.set_yticks(y)
sub.set_yticklabels(names)

sub.set_xlabel('Values', fontsize=14)
sub.set_ylabel('Name', fontsize=14)

fig.savefig('./figure.png',dpi=400)