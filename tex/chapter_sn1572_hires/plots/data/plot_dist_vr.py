#execfile('../plot_talk_defaults.py')


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
ax = axes((0.5, 0.5, 0.9, 0.9))
def plot_mchist(param1, param2 ,  ax=None, histRange=None, bins=20):
    if ax == None: ax =gca()
    mchist, xedges, yedges = np.histogram2d(param1, param2, bins=bins, range=histRange)
#    mchist = ndimage.gaussian_filter(mchist, mcBins/20)
    sortMcHist = sort(mchist.flatten())[::-1]
    cumMcSum = cumsum(sortMcHist)/sum(mchist)
    levelIDs = (cumMcSum.searchsorted(.95449), cumMcSum.searchsorted(.6826894))
    levels = [sortMcHist[item] for item in levelIDs]
#    cont = contour(xedges[:-1],
#           yedges[:-1], 
#            mchist.transpose(), levels = levels, colors='black', lws=2)
            
    levelIDs = (cumMcSum.searchsorted(.997),cumMcSum.searchsorted(.95449), cumMcSum.searchsorted(.6826894), -1)
    levels = [sortMcHist[item] for item in levelIDs]

    contf = contourf(xedges[:-1],
            yedges[:-1], 
            mchist.transpose(), levels = levels, colors=[cm.autumn(i) for i in arange(0,1,0.3)][::-1])

#rc('xtick',labelsize=15, )

if False:
    
    data_sn1572 = fromfile('besancon.npmap')
    data_sn1572 = data_sn1572.reshape(1531535, 24)

    data_sn1006 = fromfile('besancon_sn1006_1deg.npmap')
    data_sn1006 = data_sn1006.reshape(16417, 24)

    data_sn1006 = array([tuple(item) for item in data_sn1006], dtype=colNames)
    data_sn1572 = array([tuple(item) for item in data_sn1572], dtype=colNames)
    
    distData = recfromtxt('vr_dist.dat', names=True)
clf()
data = data_sn1572
1/0
datafilter = np.logical_and(data['v']>10, data['v']<20)
datafilter = np.logical_and(datafilter, data['[fe/h]']>-1)
filtData = data[datafilter]

plot_mchist(filtData['dist'], filtData['vr'], histRange = [[0,15],[-250,150]], ax = ax)
if False:
    errorbar(distData['dist'], distData['vr'], xerr=distData['ddist'], yerr=distData['dvr'], mew = 3, ls='none', color='black')
axvspan(2,3.6, color='red', alpha=0.4, linewidth=4)
if False:
    for line in distData:
        text(line['dist']+0.15, line['vr']+2, line['name'].upper(), bbox=dict(facecolor='white', alpha=0.5))
        text(line['dist']+0.15, line['vr']+2, line['name'].upper())
ax = gca()    
xlim(0,12)
xlabel('Distance [kpc]')
ylabel('vrad [km/s]')
ax.tick_params(width=4, color='orange', length=10, pad=10)
fig = gcf()
fig.subplots_adjust(0.2, 0.2, 0.98, 0.98)
c = colorbar()
c.set_ticklabels(('99 %', '95 %', '68 %'))
savefig('../dist_vr.pdf', facecolor='none')
 