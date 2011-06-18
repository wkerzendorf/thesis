
execfile('/Users/wkerzend/Documents/science/thesis/thesis/tex/thesis_plot_defaults.py')

data = loadtxt('cappellaro99.dat', usecols = (1,2,3,4,5,6))

errorkws = dict(ecolor='black',
                capsize=5,
                elinewidth=2)
                
                
fig = figure(1)
fig.clf()
barrange = arange(4)
ax1 = fig.add_subplot(311)
ax1.bar(barrange, data[:,0], yerr=data[:,1], error_kw=errorkws)
setp( ax1.get_xticklabels(), visible=False)

ax2 = fig.add_subplot(312, sharex=ax1)

ax2.bar(barrange, data[:,2], yerr=data[:,3], color='red', error_kw=errorkws)
setp( ax2.get_xticklabels(), visible=False)

ax3 = fig.add_subplot(313, sharex=ax1)
ax3.bar(barrange, data[:,4], yerr=data[:,5], color='green', error_kw=errorkws)

ax3.set_xticks(barrange+0.4)
ax3.set_xticklabels(['E-S0', 'S0a-Sb', 'Sbc-Sd', 'Others'])