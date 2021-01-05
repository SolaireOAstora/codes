import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1,200)
y = np.linspace(-1,1,400)

XX, YY = np.meshgrid(x,y,indexing='ij')


xc1 = -0.5
yc1 = 0
xc2 = 0.5
yc2 = 0
q1 = 1
q2 = 1

r1 = np.sqrt((XX-xc1)**2 + (YY-yc1)**2)
r2 = np.sqrt((XX-xc2)**2 + (YY-yc2)**2)


phi1 = -q1/r1 
radius_mask1 = 0.1
ind = np.where(r1<=radius_mask1)
ind_x = ind[0]
ind_y = ind[1]
phi1[ind_x, ind_y] = -q1/radius_mask1

phi2 = -q2/r2 
radius_mask2 = 0.1
ind = np.where(r2<=radius_mask2)
ind_x = ind[0]
ind_y = ind[1]
phi2[ind_x, ind_y] = -q2/radius_mask2

phi = phi1 + phi2



# # plot
# levels = [-10, -6, -5, -4.5, -4, -3]
# fig = plt.figure(figsize=[8,6])
# sub = fig.add_subplot(111)
# cont = sub.contour(XX, YY, phi, levels=levels, 
#     cmap = 'rainbow')
# #  colors=['red','blue'], linestyles=[':','-']

# # cb = fig.colorbar(cont, aspect=15, shrink=1)
# clabels = sub.clabel(cont, fontsize=6)

# sub.set_xlabel(r'$x$', fontsize=14)
# sub.set_ylabel(r'$y$', fontsize=14)

# plt.show()



# contourf

levels = np.linspace(-10,0,128)
fig = plt.figure(figsize=[8,6])
sub = fig.add_subplot(111)
cont = sub.contourf(XX, YY, phi, levels=levels, 
    cmap='rainbow', extend='both')
cb = fig.colorbar(cont, shrink=1, aspect=15,
    ticks = [-10,-8,-6,-4,-2,0])

levels_line = [-10, -6, -5, -4.5, -4, -3]
contlines = sub.contour(XX, YY, phi, levels=levels_line,
    colors='k', linestyles=':')
clabel = sub.clabel(contlines)

sub.set_xlabel(r'$x$', fontsize=14)
sub.set_ylabel(r'$y$', fontsize=14)

fig.savefig('./figure.png', facecolor='ivory')