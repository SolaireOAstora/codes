import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

# x = np.linspace(-1,1,201)

# y = np.exp(-x**2/2)

data = np.loadtxt('./data.csv',skiprows=1,delimiter=',')

x = data[:,0]
y = data[:,1]

# generate a figure object
fig = plt.figure()
sub = fig.add_subplot(111)

sub.plot(x,y)

sub.set_xlabel('$x$', fontsize=14)
sub.set_ylabel('$y$', fontsize=14)
# sub.set_title(r'$\Gamma$',fontsize=16)
fig.suptitle('Figure 1',fontsize=18)

# plt.show()
fig.savefig('./Figure_1.png',dpi=400)
plt.close('all')