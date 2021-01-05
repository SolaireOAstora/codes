import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from glob import glob
import os

# # read a single file
# df = pd.read_excel('./000.xlsx')

# x,y = df['x'], df['y']

# fig = plt.figure()
# sub = fig.add_subplot(111)
# sub.plot(x,y,marker='s')
# plt.show()




# use glob to search files
files = sorted(glob('./data/*.xlsx'))
print(files)

if not os.path.exists('./figure'):
    os.mkdir('./figure')


# plot 
for i in range(len(files)):
    print('Processing File #{:03d}...'.format(i))

    fig = plt.figure()
    sub = fig.add_subplot(111)

    df = pd.read_excel(files[i])

    x = df['x']
    y = df['y']

    sub.plot(x,y,marker='s',
        label='{:03d}'.format(i))

    # sub.legend()
    sub.set_xlabel(r'$x$')
    sub.set_ylabel(r'$y$')
    sub.set_title('File #{:03d}'.format(i))
    fig.tight_layout()
    fig.savefig('./figure/{:03d}.png'.format(i))
    plt.close(fig)