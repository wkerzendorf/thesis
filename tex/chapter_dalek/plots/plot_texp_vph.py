execfile('../../thesis_plot_defaults.py')

t2vph = lambda t:17648.5*np.exp(-0.0920127*t)+5436.47
clf()
texp = arange(0,30)
vph = t2vph(texp)

plot(t, vph)
xlabel(r'$t_\textrm{\small exp}$ $[days]$')
ylabel(r'$v_\textrm{\small ph}$ $[km\,s^{-1}]$')
savefig('plot_texp_vph.pdf')