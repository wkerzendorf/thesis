execfile('../../../thesis_plot_defaults.py')
europe = loadtxt('european.dat')
korea = loadtxt('korean.dat')
''
clf()
gca().invert_yaxis()

errorbar([0],[3],yerr=0.0001, lolims=[True], color='blue', mew=2)
plot(europe[:,0], europe[:,1], marker='o', color='blue', ls='none', label='European observations')
plot(korea[:,0], korea[:,1], marker='x', color='red', mew=2, ls='none', label='Korean observations')

legend(numpoints=1)
ylim(5.5,-3.5)
xlim(-5, 400)
ylabel('Magnitude')
xlabel('Days after AD1604 October 8th')
savefig('../sn1604_ancient_lc.pdf')



