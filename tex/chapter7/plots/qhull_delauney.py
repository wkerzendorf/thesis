from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FixedLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


import matplotlib.delaunay as delaunay
import matplotlib.pyplot as pp
np.random.seed(250819801106)
#generate points
npts=10
xpt=(sp.random.random_sample(npts)-0.5)*4
ypt=(sp.random.random_sample(npts)-0.5)*4
#create triangulation
circumcenters,edges,tri_points,tri_neighbors=delaunay.delaunay(xpt, ypt)
#plot using edges





fig = plt.figure(1)
fig.clf()
ax = fig.gca(projection='3d')
X = np.arange(-2, 2, 0.25)
Y = np.arange(-2, 2, 0.25)
X, Y = np.meshgrid(X, Y)
R = X**2 + Y**2 +1

surf = ax.plot_surface(X, Y, R, rstride=1, cstride=1, cmap=cm.autumn,
        linewidth=0, antialiased=False, alpha=0.5)
ax.set_zlim3d(-1.01, 1.01)

#ax.w_zaxis.set_major_locator(LinearLocator(10))
#ax.w_zaxis.set_major_formatter(FormatStrFormatter('%.03f'))
#ax.plot(xpt[edges.T][0],ypt[edges.T][1],'bo', ls='-', zs=0)
#ax.plot(xpt[edges.T][1],ypt[edges.T][1],'bo', ls='-', zs=0)
for i in xrange(20):
    ax.plot3D(xpt[edges.T][:,i],ypt[edges.T][:,i],'ro', ls='-', zs=0)
    zpts = (xpt[edges.T][:,i]**2 + ypt[edges.T][:,i]**2) + 1
    ax.plot3D(xpt[edges.T][:,i],ypt[edges.T][:,i],'bo', ls='-', zs=zpts)
#
#ax.plot(xpt[edges.T],ypt[edges.T],zs = (xpt[edges.T]**2 + ypt[edges.T]**2)+1)
#fig.colorbar(surf, shrink=0.5, aspect=5)



