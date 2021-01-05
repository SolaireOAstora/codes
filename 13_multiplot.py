import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.gridspec import GridSpec

fig = plt.figure()

# #--------------------------------
# sub1 = fig.add_subplot(221)
# sub1.set_title('Subplot 1')

# sub2 = fig.add_subplot(223)
# sub2.set_title('Subplot 2')

# # sub3 = fig.add_subplot(322)
# # sub3.set_title('Subplot 3')

# # sub4 = fig.add_subplot(324)
# # sub4.set_title('Subplot 4')

# # sub5 = fig.add_subplot(326)
# # sub5.set_title('Subplot 5')

# # fig.subplots_adjust(hspace=0.5)

# sub3 = fig.add_subplot(422)
# sub3.set_title('Subplot 3')

# sub4 = fig.add_subplot(424)
# sub4.set_title('Subplot 4')

# sub5 = fig.add_subplot(426)
# sub5.set_title('Subplot 5')

# sub6 = fig.add_subplot(428)
# sub6.set_title('Subplot 6')

# # fig.tight_layout()
# fig.subplots_adjust(hspace=0.75)
# #--------------------------------


#--------------------------------
gs = GridSpec(4,2)
sub1 = fig.add_subplot(gs[0:2,0])
sub1.set_title('Subplot 1')

sub2 = fig.add_subplot(gs[2:4,0])
sub2.set_title('Subplot 2')


sub3 = fig.add_subplot(gs[0,1])
sub3.set_title('Subplot 3')

sub4 = fig.add_subplot(gs[1,1])
sub4.set_title('Subplot 4')

sub5 = fig.add_subplot(gs[2,1])
sub5.set_title('Subplot 5')

sub6 = fig.add_subplot(gs[3,1])
sub6.set_title('Subplot 6')

fig.tight_layout()
#--------------------------------

#--------------------------------
# # gs_left = GridSpec(2,2)

# gs = GridSpec(6,2)

# sub1 = fig.add_subplot(gs[0:3,0])
# sub1.set_title('Subplot 1')
# sub2 = fig.add_subplot(gs[3:6,0])
# sub2.set_title('Subplot 2')

# # gs_right = GridSpec(3,2)

# sub3 = fig.add_subplot(gs[0:2,1])
# sub3.set_title('Subplot 3')
# sub4 = fig.add_subplot(gs[2:4,1])
# sub4.set_title('Subplot 4')
# sub5 = fig.add_subplot(gs[4:6,1])
# sub5.set_title('Subplot 5')

# fig.tight_layout()
#--------------------------------


# #--------------------------------
# gs = GridSpec(2,1)
# sub1 = fig.add_subplot(gs[0,0])
# sub2 = fig.add_subplot(gs[1,0])

# x = np.linspace(0,1,101)
# y1 = np.sin(2 * np.pi * x)
# y2 = np.cos(2 * np.pi * x)

# sub1.plot(x,y1)
# sub2.plot(x,y2)

# sub1.axvspan(0.4,0.6,color='yellow',alpha=0.5)
# sub2.axvspan(0.4,0.6,color='yellow',alpha=0.5)

# sub1.set_ylabel(r'$\sin (2 \pi x)$', fontsize=14)
# sub2.set_ylabel(r'$\cos (2 \pi x)$', fontsize=14)
# sub1.set_xlabel(r'$x$', fontsize=14)
# sub2.set_xlabel(r'$x$', fontsize=14)
# sub1.tick_params(axis='x',direction='in')
# sub1.set_xticklabels([])

# fig.subplots_adjust(hspace=0,left=0.15,right=0.95,
#     bottom=0.12,top=0.95)

# # fig.tight_layout()

plt.show()