import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

data = pd.read_excel('./income.xlsx')

year = data['Year'].to_numpy()
income_H = data.iloc[:,1].to_numpy()
income_W = data.iloc[:,2].to_numpy()

N = len(year)
x = np.arange(N)

fig = plt.figure()
sub = fig.add_subplot(111)

sub.bar(x, income_H, label='Husband', alpha=0.75,edgecolor='k',
    hatch='/')
sub.bar(x, income_W, bottom = income_H, label='Wife', alpha=0.75,
    edgecolor='k', hatch='o')

# width = 0.4
# x1 = x - width/2 
# x2 = x + width/2
# sub.bar(x1, income_H, width = width, label='Husband', alpha = 0.75,
#     edgecolor='k', hatch='//')
# sub.bar(x2, income_W, width = width, label='Wife', alpha = 0.75,
#     edgecolor='k', hatch='*')

# for i in range(N):
#     sub.text(x1[i], income_H[i], '{:.1f}'.format(income_H[i]),
#         verticalalignment='bottom', horizontalalignment='center')
#     sub.text(x2[i], income_W[i], '{:.1f}'.format(income_W[i]),
#         verticalalignment='bottom', horizontalalignment='center')

sub.set_xticks(x)
sub.set_xticklabels(year)

sub.tick_params(axis='x', length=0)

sub.spines['top'].set_visible(False)
sub.spines['right'].set_visible(False)
sub.spines['left'].set_linewidth(2)
sub.spines['bottom'].set_linewidth(2)

sub.legend()
sub.set_xlabel('Year', fontsize=15)
sub.set_ylabel('Income/$10^4$', fontsize=15)

# plt.show()
fig.tight_layout()
fig.savefig('./bar_plot_2.png', dpi=400, facecolor='wheat')