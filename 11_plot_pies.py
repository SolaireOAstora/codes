import numpy as np 
import matplotlib.pyplot as plt 

labels = ['Zhang','Wang','Li']
values = np.array([30,60,50])

# label_values = np.zeros(len(values), dtype=object)
# for i in range(len(label_values)):
#     label_values[i] = (labels[i]).center(10) + '\n' + ('{:d}'.format(values[i])).center(10)

# print(label_values)

def func(pct,allvals):
    absolute = int(pct/100 * np.sum(allvals))
    return '{:.1f}%\n{:d}'.format(pct, absolute)

fig = plt.figure()
sub = fig.add_subplot(111)

wedges, texts, autotexts = sub.pie(values,
    labels=labels, 
    colors= ['C0','C1','C2'],
    rotatelabels=False,
    labeldistance=1.2, startangle=0,
    counterclock=True, explode=[0,0,0.05],
    autopct=lambda x:func(x,values), textprops = 
    dict(fontsize=15), radius = 1.0,
    shadow = True, wedgeprops = dict(
        edgecolor='w', width=1.0
    ))

for i in range(len(autotexts)):
    autotexts[i].set_color('w')
    texts[i].set_size(20)
    texts[i].set_weight('bold')

sub.legend()
fig.suptitle('Pies', fontsize=16)
fig.tight_layout()
plt.show()
# fig.savefig('./figure.png',dpi=400,facecolor='lightcyan')