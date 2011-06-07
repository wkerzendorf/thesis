import numpy as n, pylab as p, time
def _angle_to_point(point, centre):
    '''calculate angle in 2-D between points and x axis'''
    delta = point - centre
    res = n.arctan(delta[1] / delta[0])
    if delta[0] < 0:
        res += n.pi
    return res


def _draw_triangle(p1, p2, p3, **kwargs):
    tmp = n.vstack((p1,p2,p3))
    x,y = [x[0] for x in zip(tmp.transpose())]
    p.fill(x,y, **kwargs)
    #time.sleep(0.2)


def area_of_triangle(p1, p2, p3):
    '''calculate area of any triangle given co-ordinates of the corners'''
    return n.linalg.norm(n.cross((p2 - p1), (p3 - p1)))/2.


def convex_hull(points, graphic=True, smidgen=0.0075):
    '''Calculate subset of points that make a convex hull around points

Recursively eliminates points that lie inside two neighbouring points until only convex hull is remaining.

:Parameters:
    points : ndarray (2 x m)
        array of points for which to find hull
    graphic : bool
        use pylab to show progress?
    smidgen : float
        offset for graphic number labels - useful values depend on your data range

:Returns:
    hull_points : ndarray (2 x n)
        convex hull surrounding points
'''
    if graphic:
        p.clf()
        p.plot(points[0], points[1], 'ro')
    n_pts = points.shape[1]
    assert(n_pts > 5)
    centre = points.mean(1)
    if graphic: p.plot((centre[0],),(centre[1],),'bo')
    angles = n.apply_along_axis(_angle_to_point, 0, points, centre)
    pts_ord = points[:,angles.argsort()]
    if graphic:
        for i in xrange(n_pts):
            p.text(pts_ord[0,i] + smidgen, pts_ord[1,i] + smidgen, \
                   '%d' % i)
    pts = [x[0] for x in zip(pts_ord.transpose())]
    prev_pts = len(pts) + 1
    k = 0
    while prev_pts > n_pts:
        prev_pts = n_pts
        n_pts = len(pts)
        if graphic: p.gca().patches = []
        i = -2
        while i < (n_pts - 2):
            Aij = area_of_triangle(centre, pts[i],     pts[(i + 1) % n_pts])
            Ajk = area_of_triangle(centre, pts[(i + 1) % n_pts], \
                                   pts[(i + 2) % n_pts])
            Aik = area_of_triangle(centre, pts[i],     pts[(i + 2) % n_pts])
            if graphic:
                _draw_triangle(centre, pts[i], pts[(i + 1) % n_pts], \
                               facecolor='blue', alpha = 0.2)
                _draw_triangle(centre, pts[(i + 1) % n_pts], \
                               pts[(i + 2) % n_pts], \
                               facecolor='green', alpha = 0.2)
                _draw_triangle(centre, pts[i], pts[(i + 2) % n_pts], \
                               facecolor='red', alpha = 0.2)
            if Aij + Ajk < Aik:
                if graphic: p.plot((pts[i + 1][0],),(pts[i + 1][1],),'go')
                del pts[i+1]
            i += 1
            n_pts = len(pts)
        k += 1
    return n.asarray(pts)


#### my code ###
np.random.seed(250819801110)

x_points = np.random.random(20)
y_points = np.random.random(20)

points = np.vstack((x_points, y_points)).transpose()
fig = figure(num=1, figsize=(8, 6))
fig.clf()

def construct_line(point1, point2):
    m = (point1[1]-point2[1])/(point1[0]-point2[0])
    t = point1[1] - m*point1[0]
    return m,t

#step1
ax = fig.add_subplot(111)   
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)


ax.plot(x_points, y_points, 'bo')


fig.savefig('qhull_1.pdf')

#step2


x_min_id = x_points.argmin()
x_max_id = x_points.argmax()



m, t = construct_line(points[x_min_id], points[x_max_id])

ax.plot(x_points[[x_min_id, x_max_id]], y_points[[x_min_id, x_max_id]], color='orange', ls='-', lw=2)

mask1 = (m*x_points+t - y_points) > 0
ax.plot(x_points[mask1], y_points[mask1], 'ro')
savefig('qhull_2.pdf')

#step3

sel_point1_id = np.argmin(m*x_points+t - y_points)

ax.plot(x_points[[x_min_id, sel_point1_id, x_max_id, ]], y_points[[x_min_id, sel_point1_id, x_max_id ]], color='orange', ls='-', lw=2)


m_2, t_2 = construct_line(points[x_min_id], points[sel_point1_id])
m_3, t_3 = construct_line(points[x_max_id], points[sel_point1_id])

mask2 = (m_2*x_points+t_2 - y_points) > 0
mask3 = (m_3*x_points+t_3 - y_points) > 0

ax.plot(x_points[np.logical_not(mask2)], y_points[np.logical_not(mask2)], 'yo')
ax.plot(x_points[np.logical_not(mask3)], y_points[np.logical_not(mask3)], 'co')

ax.plot(x_points[[x_min_id, sel_point1_id, x_max_id, ]], y_points[[x_min_id, sel_point1_id, x_max_id ]], 'ko')
fig.savefig('qhull_3.pdf')

#convex hull
fig.clf()

hull_pts = convex_hull(points.transpose(), graphic=False)
mask = [0,1,2,3,4,5,6,7]
chull = mpl.patches.Polygon(hull_pts[mask], fc='none', ec='orange', lw=3)

ax = fig.add_subplot(111)   
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

ax.plot(x_points, y_points, 'bo')
ax.add_patch(chull)

savefig('qhull_final.pdf')


