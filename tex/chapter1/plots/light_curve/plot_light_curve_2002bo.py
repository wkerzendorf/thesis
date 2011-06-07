execfile('/Users/wkerzend/Documents/science/thesis/thesis/tex/thesis_plot_defaults.py')

from scipy import interpolate
bphot = loadtxt('2002bo_b.dat')
vphot = loadtxt('2002bo_v.dat')
rphot = loadtxt('2002bo_r.dat')
iphot = loadtxt('2002bo_i.dat')

fig = pylab.figure(1)
fig.clf()

ax = fig.add_subplot(111)

bmax = 2452358. -2

bphot[:,0] -= bmax
vphot[:,0] -= bmax
rphot[:,0] -= bmax
iphot[:,0] -= bmax

newtime = arange(-20,100,0.1)
sfactor = .1
kfactor = 3
sbphot = interpolate.splev(newtime, 
            interpolate.splrep(bphot[:,0], bphot[:,1], s=.2, k=kfactor), )
svphot = interpolate.splev(newtime, 
            interpolate.splrep(vphot[:,0], vphot[:,1], s=.2, k=kfactor), )
srphot = interpolate.splev(newtime, 
            interpolate.splrep(rphot[:,0], rphot[:,1], s=sfactor, k=kfactor))
siphot = interpolate.splev(newtime, 
            interpolate.splrep(iphot[:,0], iphot[:,1], s=sfactor, k=kfactor))


dist_mod = 33.7
ax.plot(newtime, sbphot - dist_mod, ls='-', label='b', color='k', lw=4)
ax.plot(newtime, svphot - dist_mod, ls='-', label='v', color='b', lw=4)
ax.plot(newtime, srphot - dist_mod, ls='-', label='r', color='g', lw=4)
ax.plot(newtime, siphot - dist_mod, ls='-', label='i', color='y', lw=4)

ax.axvspan(-20, -5, color='red', alpha=0.3)
ax.axvspan(-5, 15, color='blue', alpha=0.3)
ax.axvspan(15, 50, color='green', alpha=0.3)
ax.axvspan(50, 100, color='yellow', alpha=0.3)

text(-12.5, -12, 'Rise Phase', rotation='vertical', verticalalignment='bottom')
text(5, -12, 'Maximum Phase', rotation='vertical', verticalalignment='bottom')
text(32.5, -12, 'NIR Second Maximum', rotation='vertical', verticalalignment='bottom')
text(75, -12, 'Late Decline', rotation='vertical', verticalalignment='bottom')


legend()
ax.axvline(0, color='k')

ax.invert_yaxis()
ax.set_xlim(-20,100)
ax.set_xlabel(r't relative to $B_\textrm{max}$')
ax.set_ylabel('Magnitude')

savefig('../lightcurve_2002bo.pdf')
