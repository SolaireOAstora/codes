import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0,10,1001)
y1 = x
y2 = 95 + 5 * np.cos(4*np.pi * x/10)

fig = plt.figure(figsize=[8,4.5])
fig.patch.set_facecolor('xkcd:wheat')
fig.patch.set_alpha(0.5)
sub = fig.add_subplot(111)
# sub.set_facecolor('green')
sub.plot(x,y1, label=r'$y=x$')
sub.set_xlabel(r'$x$', fontsize=15)
sub.set_ylabel(r'$y1$', fontsize=15, color='C0')
sub.tick_params(which='both', axis='y', colors='C0')
sub.legend(loc=[0.2,0.8],fontsize=15)
sub.axhspan(4,6,color='yellow',alpha=0.5)
sub.spines['left'].set_color('C0')

sub2 = sub.twinx()
sub2.plot(x,y2, label=r'$y=95 + 5 \cos (\frac{2}{5} \pi x)$',color='C1')
sub2.legend(loc='lower center',fontsize=15)
sub2.set_ylabel(r'$y2$', fontsize=15, color='C1')
sub2.tick_params(which='both', axis='y', colors='C1')
sub2.axvspan(30/8,50/8,color='green',alpha=0.5)
sub2.text(0.5,0.85,'Sample Plot',transform=sub.transAxes,
    fontsize=30,ha='center',va='center',fontweight='bold',
    fontstyle='italic',rotation=10,color='red',
    bbox=dict(facecolor='None',edgecolor='red',linestyle='--',
        linewidth=3))

sub2.spines['right'].set_color('C1')
sub2.spines['left'].set_color('C0')

# plt.show()

fig.savefig('./figure.png',dpi=400,
    facecolor=fig.get_facecolor())
plt.close(fig)



'''
x = np.linspace(0,1,101)

y = np.cos(2 * np.pi * x)

fig = plt.figure()
sub = fig.add_subplot(111)
sub.plot(x,y)
# sub.fill_between([0.25, 0.75], [-1.2, -1.2], [1.2, 1.2],
#     color='yellow', alpha = 0.5 )

sub.text(0.5 , 0.2, r'$y=\cos (2 \pi x)$', fontsize=15,
    color='red', horizontalalignment='center',
    verticalalignment='center', transform=sub.transAxes,
    rotation = 45, bbox = dict(edgecolor='green',
        facecolor='None', linestyle='--', linewidth=2))

sub.axhline(y=0, color='k', linewidth=0.5)
sub.set_ylim([-1.2, 1.2])
sub.set_xlabel(r'$x$', fontsize=15)
sub.set_ylabel(r'$y$', fontsize=15)
plt.show()
'''