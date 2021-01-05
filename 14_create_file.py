import numpy as np 
import pandas as pd 

nFiles = 5

x = np.linspace(0,1,11)
N = len(x)
for i in range(nFiles):
    y = np.random.rand(N)

    df = pd.DataFrame(np.array([x,y]).T, 
        columns=['x', 'y'])

    df.to_excel('{:03d}.xlsx'.format(i), index=False)