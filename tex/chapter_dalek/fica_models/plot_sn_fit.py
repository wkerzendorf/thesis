from pyspec import oned
execfile('/Users/wkerzend/Documents/science/thesis/thesis/tex/thesis_plot_defaults.py')
plotBF = True
plotLumDelta = True
plotVphDelta = True
plotNiDelta = True
intensity_label = r'$F_\lambda[\textrm{erg}\,s^{-1}\,cm^{-2}\,\textrm{\AA}^{-1}]$'
origspec = oned.onedspec.from_ascii('origspec_2002bo_-10.dat')
if plotBF:
    clf()
    origspec = oned.onedspec.from_ascii('origspec_2002bo_-10.dat')
    origspec = origspec.shift_velocity(z=0.0042)
    bestfit = oned.onedspec.from_ascii('bf2002bo-10/spct.dat', usecols=(0,2))
    
    plot(origspec.wave, origspec.flux, 'k-', label='observed spectrum')
    plot(bestfit.wave, bestfit.flux, 'r-', label='fitted spectrum')
    
    
    xlim(2500, 9000)
    xlabel('Wavelength [\AA]')
    ylabel(intensity_label)
    legend()
    savefig('../plots/bf2002bo-10.pdf')

if plotLumDelta:
    clf()
    lolum = oned.onedspec.from_ascii('2002bo-10_lolum/spct.dat', usecols=(0,2))
    hilum = oned.onedspec.from_ascii('2002bo-10_hilum/spct.dat', usecols=(0,2))
    
    plot(origspec.wave, origspec.flux, 'k-')
    plot(lolum.wave, lolum.flux, 'b-', label='$\Delta\log{(L/L_\odot)}=-0.2$')
    plot(hilum.wave, hilum.flux, 'r-', label='$\Delta\log{(L/L_\odot)}=+0.2$')

    xlim(2500, 9000)
    xlabel('Wavelength [\AA]')
    ylabel(intensity_label)
    
    legend()
    savefig('../plots/bf2002bo-10_lum.pdf')

if plotVphDelta:
    clf()
    lovph = oned.onedspec.from_ascii('2002bo-10_lovph/spct.dat', usecols=(0,2))
    hivph = oned.onedspec.from_ascii('2002bo-10_hivph/spct.dat', usecols=(0,2))
    
    plot(origspec.wave, origspec.flux, 'k-')
    plot(lovph.wave, lovph.flux, 'b-', label=r'$v_\textrm{\small ph} - 4000\,km\,s^{-1}$')
    plot(hivph.wave, hivph.flux, 'r-', label=r'$v_\textrm{\small ph} + 5000\,km\,s^{-1}$')
    legend()
    xlim(2500, 9000)
    xlabel('Wavelength [\AA]')
    ylabel(intensity_label)
    legend()
    savefig('../plots/bf2002bo-10_vph.pdf')
    
if plotNiDelta:
    clf()
    loni = oned.onedspec.from_ascii('2002bo-10_loni/spct.dat', usecols=(0,2))
    hini = oned.onedspec.from_ascii('2002bo-10_hini/spct.dat', usecols=(0,2))
    
    plot(origspec.wave, origspec.flux, 'k-')
    plot(loni.wave, loni.flux, 'b-', label='$Fe=Ni=10\%$')
    plot(hini.wave, hini.flux, 'r-', label='$Fe=Ni=10^{-5}\%$')
    
    xlim(2500, 9000)
    xlabel('Wavelength [\AA]')
    ylabel(intensity_label)
    legend()
    savefig('../plots/bf2002bo-10_ige.pdf')
    