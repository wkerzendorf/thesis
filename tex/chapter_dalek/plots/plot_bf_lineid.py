from pyfica import fileio
execfile('/Users/wkerzend/Documents/science/thesis/thesis/tex/thesis_plot_defaults.py')


llist = fileio.sbibfile('bf2002bo-10_sbib.dat').read_data()['llist']

testlines = llist[np.logical_and(llist['shift'] > 3500, llist['eqw'] > 50)]


plot_lines = (('Ca II', 3715, 1e-15),
            ('Si II', 3972, 5e-15),
            ('Mg II', 4322, 3.8e-15),
            ('Si II', 4826, 3e-15),
            ('S II', 5205, 4e-15),
            ('S II', 5360, 3e-15),
            ('Si II', 6065, 2e-15),
            ('O I', 7500, 1.5e-15),
            ('Ca II', 8200, 1e-15))

intensity_label = r'$F_\lambda[\textrm{erg}\,s^{-1}\,cm^{-2}\,\textrm{\AA}^{-1}]$'
clf()
origspec = oned.onedspec.from_ascii('origspec_2002bo_-10.dat').shift_velocity(z=0.0042)
bestfit = oned.onedspec.from_ascii('bf2002bo-10.dat', usecols=(0,2))

plot(origspec.wave, origspec.flux, 'k-', label='observed spectrum')
plot(bestfit.wave, bestfit.flux, 'r-', label='fitted spectrum')
lastline = 0.
for line in plot_lines:

    text(line[1], line[2]-.4e-15, line[0], horizontalalignment='center', verticalalignment='top')
    plot((line[1],line[1]), (line[2], line[2]-.4e-15), 'k-')
xlim(2500, 9000)
xlabel('Wavelength [\AA]')
ylabel(intensity_label)
legend()
savefig('bf2002bo-10_lineid.pdf')