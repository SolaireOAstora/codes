import numpy as np 
import matplotlib.pyplot as plt 
import datetime


x = np.sin( 2*np.pi * np.arange(0,25) / 25)

dt0 = datetime.datetime(2020,5,10,0,30)
dt1 = dt0 + datetime.timedelta(days=1, minutes=1)

dt_arr = (np.arange(dt0, dt1, 
    datetime.timedelta(hours=1))).astype(object)


fig = plt.figure()
sub = fig.add_subplot(111)
sub.plot(dt_arr, x)
sub.set_xlabel('time', fontsize=15)
sub.set_ylabel(r'$x$', fontsize=15)

xticks = (np.arange(dt0, dt1, 
    datetime.timedelta(hours=6))).astype(object)
sub.set_xticks(xticks)

xticks_minor = (np.arange(dt0, dt1, 
    datetime.timedelta(hours=1))).astype(object)
sub.set_xticks(xticks_minor, minor=True)

xticklabels = np.zeros(len(xticks), dtype=object)
for i in range(len(xticks)):
    xticklabels[i] = xticks[i].strftime('%H:%M')
sub.set_xticklabels(xticklabels)

sub.set_title(r'Temperature on ' + dt0.strftime('%Y-%m-%d'),
    fontsize=15)

plt.show()