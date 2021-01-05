import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
from datetime import datetime 

data = pd.read_csv('https://raw.githubusercontent.com/SolaireOAstora/PythonPlotDemoMaterials/master/NYTemperature2019.csv')


date_str = data['DATE'].to_numpy()
TMIN = data['TMIN'].to_numpy()
TMAX = data['TMAX'].to_numpy()
TAVG = data['TAVG'].to_numpy()

nrec = len(TAVG)


dt_str_arr = np.zeros(nrec, dtype=object)
yday_arr = np.zeros(nrec, dtype=int)
month_arr = np.zeros(nrec, dtype=int)
for i in range(nrec):
    dt = datetime.strptime(date_str[i], '%Y-%m-%d')
    dt_str_arr[i] = dt.strftime('%b-%d')

    dt_struct = dt.timetuple()
    yday_arr[i] = dt_struct.tm_yday
    month_arr[i] = dt_struct.tm_mon


TAVG_monthly = np.zeros(12)
rms_monthly = np.zeros(12)
yday_monthly = np.zeros(12, dtype=int)

yday_ticks = np.zeros(12, dtype=int)
yday_labels = np.zeros(12, dtype=object)

for imonth in range(12):
    dt = datetime(2019, imonth+1, 1)
    yday_ticks[imonth] = dt.timetuple().tm_yday
    yday_labels[imonth] = dt.strftime('%b-%d')

    idx = (np.where(month_arr == (imonth+1)))[0]

    TAVG_monthly[imonth] = np.mean(TAVG[idx])
    rms_monthly[imonth] = np.std(TAVG[idx])

    yday_monthly[imonth] = (yday_arr[idx[0]] + yday_arr[idx[-1]])/2

fig = plt.figure(figsize=[8,5])
sub = fig.add_subplot(111)

sub.scatter(yday_arr, TAVG, s=15, c='C1', alpha=0.5)
sub.errorbar(yday_monthly, TAVG_monthly, yerr=rms_monthly,
    marker='s', capsize=6, elinewidth=2)

sub.set_xlabel('Day of Year', fontsize=15)
sub.set_ylabel('Temperature of NY', fontsize=15)

sub.set_xticks(yday_ticks)
sub.set_xticklabels(yday_labels)
sub.tick_params(axis='x', labelrotation=30)

fig.tight_layout()

# plt.show()
fig.savefig('./figure.png', dpi=400, facecolor='azure')


'''
yerr = np.zeros([2,nrec])

yerr[0,:] = TAVG - TMIN 
yerr[1,:] = TMAX - TAVG


# plot -----------
fig = plt.figure(figsize=[8,5])
sub = fig.add_subplot(111)

xerr = np.zeros([2,7]) + 0.3
sub.errorbar(np.arange(0,7), TAVG[0:7], yerr = yerr[:, 0:7],
    xerr = xerr, marker='s', capsize=6, elinewidth=2, capthick=3,
    linestyle='none')

sub.set_xticks(np.arange(0,7))
sub.set_xticklabels(dt_str_arr[0:7])

sub.set_xlabel('Date', fontsize=15)
sub.set_ylabel('Temperature of NY', fontsize=15)

plt.show()
'''