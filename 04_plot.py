import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

df = pd.read_excel('./data.xlsx', sheet_name = 'Sheet1')

# plot 

fig = plt.figure()
sub = fig.add_subplot(111)
sub.plot(df['x'], df['y'], marker='*', markersize=12)

sub.set_xlabel(r'$x$', fontsize=14)
sub.set_ylabel(r'$y$', fontsize=14)
sub.set_title(r'Plot 1', fontsize=14)
fig.suptitle(r'Figure 1', fontsize=15)

plt.show()
plt.close(fig)