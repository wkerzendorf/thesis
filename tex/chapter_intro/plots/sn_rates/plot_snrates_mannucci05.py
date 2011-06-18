execfile('/Users/wkerzend/Documents/science/thesis/thesis/tex/thesis_plot_defaults.py')

data = loadtxt('snrate_mannucci05.dat',)

errorkws = dict(ecolor='black',
                capsize=5,
                elinewidth=2)
fig = figure(1)
fig.clf()
markersize = 20
galrange = arange(4)
limsargs= [False]*4
limsargs[0]=True
errorbar(galrange, data[:,0], yerr=data[:,1:3].transpose(), 
         label='Ia', ms=markersize,
         capsize=5, mew=2, color='black')
errorbar(galrange-0.05, data[:,3], yerr=data[:,4:6].transpose(), uplims=limsargs,
        label='Ib/c', ms=markersize,
        capsize=5, mew=2, color='blue')
errorbar(galrange+0.05, data[:,6], yerr=data[:,7:9].transpose(),
         uplims=limsargs, label='II', ms=markersize,
         capsize=5, mew=2, color='red')


semilogy()
legend(loc='lower right')
xlim(-0.5, 3.5)
gca().set_xticks(galrange)
gca().set_xticklabels(['E/S0', 'S0a/b', 'Sbc/Sd', 'Irr'])
ylabel(r'$1\,SN\ (100\,\textrm{yr})^{-1}\ (10^{10}\,M_\odot)^{-1}$')

savefig('../snrates_mannucci05.pdf')