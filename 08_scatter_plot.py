import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from datetime import datetime


data_LA = pd.read_csv('https://raw.githubusercontent.com/SolaireOAstora/PythonPlotDemoMaterials/master/LATemperature2019.csv')

data_NY = pd.read_csv('https://raw.githubusercontent.com/SolaireOAstora/PythonPlotDemoMaterials/master/NYTemperature2019.csv')

# process LA data
date_LA_str = data_LA['DATE'].to_numpy()
TAVG_LA = data_LA['TAVG'].to_numpy()

nrec = len(TAVG_LA)

date_LA = np.zeros(nrec, dtype=object)
for i in range(nrec):
    date_LA[i] = datetime.strptime(date_LA_str[i], '%Y-%m-%d')

doy_LA = np.zeros(nrec)
for i in range(nrec):
    doy_LA[i] = date_LA[i].timetuple().tm_yday

# sort the data according to time
argsort_idx = np.argsort(doy_LA)

doy_LA = doy_LA[argsort_idx]
TAVG_LA = TAVG_LA[argsort_idx]


# process NY data
date_NY_str = data_NY['DATE'].to_numpy()
TAVG_NY = data_NY['TAVG'].to_numpy()

nrec = len(TAVG_NY)

date_NY = np.zeros(nrec, dtype=object)
for i in range(nrec):
    date_NY[i] = datetime.strptime(date_NY_str[i], '%Y-%m-%d')

doy_NY = np.zeros(nrec)
for i in range(nrec):
    doy_NY[i] = date_NY[i].timetuple().tm_yday

# sort the data according to time
argsort_idx = np.argsort(doy_NY)

doy_NY = doy_NY[argsort_idx]
TAVG_NY = TAVG_NY[argsort_idx]

#plot-----------------------------
fig = plt.figure()
sub = fig.add_subplot(111)

# # directly plot
# sub.plot(TAVG_LA, TAVG_NY, linestyle='none', marker='o')

# use scatter
scat = sub.scatter(TAVG_LA, TAVG_NY, marker='o', c=doy_LA, 
    cmap='twilight' )

cb = fig.colorbar(scat, shrink=1, aspect=12)
cb.ax.set_ylabel('day of year', fontsize=14)
cb.set_ticks([1,180,360])
cb.ax.set_yticklabels(['001','180','360'], fontsize=14)

sub.set_xlabel(r'Temperature of LA', fontsize=15)
sub.set_ylabel(r'Temperature of NY', fontsize=15)
sub.set_xlim([5,30])
sub.set_ylim([-15,35])

# plt.show()
fig.savefig('./figure.png',dpi=400)
plt.close(fig)