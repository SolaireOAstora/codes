import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0,1,100)
y = 10 * x
y2 = 8 * x 
y3 = 10 - 5 * x

fig = plt.figure()
sub = fig.add_subplot(111)
line1, = sub.plot(x,y, label=r'$y=10x$')
line2, = sub.plot(x,y2, label=r'$y=8x$')
line3, = sub.plot(x,y3, label=r'$y=10-5x$')

sub.axhline(y=20/3, color='red', linestyle='-.')
sub.axvline(x=2/3, color='red', linestyle='-.')

leg1 = sub.legend(handles=[line1, line3])
sub.add_artist(leg1)

sub.legend(handles=[line2], loc='lower center')

sub.set_xlabel(r'$x$', fontsize=15)
sub.set_ylabel(r'$y$', fontsize=15)

sub.set_xticks([0,0.5,1.0])
sub.set_xticks(np.arange(0,1.01,0.1), minor=True)

sub.grid(linestyle='--', which='both')

plt.show()
fig.savefig('./figure.png', dpi=400)