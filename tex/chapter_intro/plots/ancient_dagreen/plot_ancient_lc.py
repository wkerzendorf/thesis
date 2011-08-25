execfile('../../../thesis_plot_defaults.py')
europe = loadtxt('european.dat')
korea = loadtxt('korean.dat')
ia_tmpl = loadtxt('../li2011_snrates/lc-Ia.01.txt')
iip_tmpl = loadtxt('../li2011_snrates/lc-IIP.txt')
iil_tmpl = loadtxt('../li2011_snrates/lc-IIL.txt')

clf()
gca().invert_yaxis()

errorbar([0],[3],yerr=0.0001, lolims=[True], color='blue', mew=2)
plot(europe[:,0], europe[:,1], marker='o', color='blue', ls='none', label='European observations')
plot(korea[:,0], korea[:,1], marker='x', color='red', mew=2, ls='none', label='Korean observations')
plot(ia_tmpl[:,0]+20, ia_tmpl[:,1]-3, label='Light Curve Template SN Ia')
plot(iip_tmpl[:,0]+5, iip_tmpl[:,1]-3, label='Light Curve Template SN IIP')
plot(iil_tmpl[:,0]+5, iil_tmpl[:,1]-3, label='Light Curve Template SN IIL')
legend(numpoints=1)
ylim(5.5,-3.5)
xlim(-5, 400)
ylabel('Magnitude')
xlabel('Days after AD1604 October 8th')
savefig('../sn1604_ancient_lc.pdf')



