execfile('/Users/wkerzend/Documents/science/thesis/thesis/tex/thesis_plot_defaults.py')

import matplotlib.delaunay as triang
import pylab
import numpy

np.random.seed(250819801106)


# 10 random points (x,y) in the plane
x,y =  numpy.array(numpy.random.standard_normal((2,15)))
cens,edg,tri,neig = triang.delaunay(x,y)
clf()
for t in tri:
 # t[0], t[1], t[2] are the points indexes of the triangle
 t_i = [t[0], t[1], t[2], t[0]]
 pylab.plot(x[t_i],y[t_i], color='k')
ax = gca()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.axes.set_frame_on(False)
savefig('simple_delauney.pdf')
pylab.plot(x,y,'ko')
