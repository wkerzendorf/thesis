import aplpy,ephem
data=recfromtxt('SN1006DB.dat',converters={1:ephem.hours,2:ephem.degrees},names=True)

ra=data['ra']/ephem.degree
dec=data['dec']/ephem.degree
clf()
dss=aplpy.FITSFigure('dss.fits',figure=figure(1))
dss.show_grayscale(invert='True')
dss.show_contour('vla.fits',colors='black',linewidths=3,linestyles='-')
dss.show_markers(ra,dec,s=50,zorder=20,linewidths=3)

sm_star_coord = (ephem.hours('15:02:53.15')/ephem.degree, ephem.degrees('-41:59:16.7')/ephem.degree)

xlim(418.25256783519171, 976.38449164673648)
ylim(1.3028136019328969, 565.40172799399215)
dss.show_markers(ra,dec,s=20,zorder=20,linewidths=3)
dss.show_markers([sm_star_coord[0]], [sm_star_coord[1]], color='black')
title('SN1006 DSS Image with VLA Overlay (Overlay is cutoff)',fontsize=20)
ax=gca()
ax.set_xlabel("RA (J2000)",fontsize=20)
ax.set_ylabel("Dec (J2000)",fontsize=20)
for item in ax.get_xticklabels():
	item.set_fontsize(15)
for item in ax.get_yticklabels():
	item.set_fontsize(15)
savefig('sn1006_overlay.pdf')
savefig('sn1006_overlay.png')

