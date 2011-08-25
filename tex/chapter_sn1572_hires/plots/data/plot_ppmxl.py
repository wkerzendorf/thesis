from scipy import ndimage
execfile('../../../thesis_plot_defaults.py')
colNames = [('dist', float64),
 ('mv', float64),
 ('cl', float64),
 ('typ', float64),
 ('ltef', float64),
 ('logg', float64),
 ('age', float64),
 ('mass', float64),
 ('b-v', float64),
 ('u-b', float64),
 ('v-i', float64),
 ('v-k', float64),
 ('v', float64),
 ('mux', float64),
 ('muy', float64),
 ('vr', float64),
 ('uu', float64),
 ('vv', float64),
 ('ww', float64),
 ('[fe/h]', float64),
 ('l', float64),
 ('b', float64),
 ('av', float64),
 ('mbol', float64)]

if False:
    data_sn1572 = fromfile('besancon.npmap')
    data_sn1572 = data_sn1572.reshape(1531535, 24)
    data_sn1572 = array([tuple(item) for item in data_sn1572], dtype=colNames)
    dist_filter = np.logical_and(data_sn1572['dist']>3.7-1.5, data_sn1572['dist']<3.7+1.5)
        
    
mux, muy, emux, emuy = loadtxt('tap_ppmxl_3.dat', unpack=1, usecols=(0,1,2,3))
mux*=3.6e6
muy*=3.6e6
emux*=3.6e6
emuy*=3.6e6

velfilter = (mux**2+muy**2)<50**2
#mux = mux[velfilter]
#muy = muy[velfilter]
#emux = emux[velfilter]
#emuy = emuy[velfilter]
mux = mux-mean(mux[velfilter])
muy = muy-mean(muy[velfilter])
    
    
filtdata = data_sn1572[dist_filter]
def plot_mchist(param1, param2 ,  ax=None, histRange=None, bins=20):
    if ax == None: ax =gca()
    mchist, xedges, yedges = np.histogram2d(param1, param2, bins=bins, range=histRange)
    mchist = ndimage.gaussian_filter(mchist, bins/50)
    sortMcHist = sort(mchist.flatten())[::-1]
    cumMcSum = cumsum(sortMcHist)/sum(mchist)
    levelIDs = (cumMcSum.searchsorted(.95449), cumMcSum.searchsorted(.6826894))
    levels = [sortMcHist[item] for item in levelIDs]
#    cont = contour(xedges[:-1],
#           yedges[:-1], 
#            mchist.transpose(), levels = levels, colors='black', lws=2)
            
    levelIDs = (cumMcSum.searchsorted(.997),cumMcSum.searchsorted(.95449), cumMcSum.searchsorted(.6826894))
    levels = [sortMcHist[item] for item in levelIDs]

    contf = contour(xedges[:-1],
            yedges[:-1], 
            mchist.transpose(), levels = levels, colors='black',linewidths=3, zorder=10)
    return xedges, yedges, mchist
    
clf()
xedges, yedges, mchist = plot_mchist(filtdata['mux']*10, filtdata['muy']*10)
#errorbar(mux, muy, xerr=emux, yerr=emuy, color='r', ls='none')
plot(mux, muy, 'ro')
plot([-2.5], [-4.22], marker='x', color='blue', mew=8, ms=30, alpha=0.8, zorder=20)
xlim(-50,50)
ylim(-50,50)
xlabel(r'$\mu_\alpha$ [mas/yr]')
ylabel(r'$\mu_\delta$ [mas/yr]')
errorbar([-40], [-40], xerr=4, yerr=4, color='r', elinewidth=2, mew=2)
text(-44, -32, 'Typical PPMXL Error', color='red', bbox=dict(facecolor='white', ec='white'))
draw()
savefig('../ppmxl_besancon_plot.pdf')
