execfile('../../../thesis_plot_defaults.py')
from scipy import ndimage
data = recfromtxt('plotcomp09-Kerzendorf02.dat', names=True)
clf()
mcBins=20
def plot_mchist(mcparam1, mcparam2 ,  ax=None, histRange=None):
    if ax == None: ax =gca()
    mchist, xedges, yedges = np.histogram2d(mcparam1, mcparam2, bins=mcBins, range=histRange)
#    return mchist
    mchist = ndimage.gaussian_filter(mchist, mcBins/30.)

    sortMcHist = sort(mchist.flatten())[::-1]
    mcSize = sum(sortMcHist)
    cumMcSum = cumsum(sortMcHist)/mcSize
    levelIDs = (cumMcSum.searchsorted(.997), cumMcSum.searchsorted(.95449), cumMcSum.searchsorted(.6826894))
    levels = [sortMcHist[item] for item in levelIDs]
#    cont = contour(xedges[:-1],
#           yedges[:-1], 
#            mchist.transpose(), levels = levels, colors='black', lws=2)
            
    levelIDs = (cumMcSum.searchsorted(.997),cumMcSum.searchsorted(.95449), cumMcSum.searchsorted(.6826894), -1)
    levels = [sortMcHist[item] for item in levelIDs]

    
    contf = contourf(xedges[:-1],
            yedges[:-1], 
            mchist.transpose(), levels = levels, colors=[cm.gray(i) for i in (0.2, 0.5, 0.8)[::-1]])

    return levels


levels=plot_mchist(data['vr'], data['logg'])
xlabel(r'$v_\textrm{\small escape}$ [km\,s$^{-1}$]')
ylabel('log(g)')

savefig('../theo_vrad.pdf', facecolor='none')
clf()

plot_mchist(data['vrot'], data['logg'])
xlabel(r'$v_\textrm{\small rot}$ [km\,s$^{-1}$]')
ylabel(r'\log(g)')

savefig('../theo_vrot.pdf', facecolor='none')
