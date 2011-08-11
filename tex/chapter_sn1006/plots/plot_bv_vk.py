#loading data
import sqlite3
import numpy as np

execfile('../../thesis_plot_defaults.py')
if True:
    conn = sqlite3.connect('data/phot_db.db3')
    selectstmt = """select 
            b, berr, v, verr, k, kerr, j, jerr, qflag, name
            from sn1006_nfilter_isocor
            inner join twomass
                on sn1006_nfilter_isocor.id=twomass.id
            inner join sn1006_stars
                on sn1006_stars.id=sn1006_nfilter_isocor.id
            where b is not null and v is not Null and k is not Null and j is not Null"""
    color_data = zip(*conn.execute(selectstmt).fetchall())
    qflag = color_data[-2]
    name = color_data[-1]
    b, berr, v, verr, k, kerr, j, jerr = array(color_data[:-2])                
    conn.close()
    
clf()

bv = b-v
vk = v-k
bverr = np.sqrt(berr.astype(float64)**2+verr.astype(float64)**2)
kerr=array([item if item !=None else 0.4 for item in kerr])
vkerr = np.sqrt(verr.astype(float64)**2 + kerr**2)
upperlimit = kerr>0.35
kerr[upperlimit]=None
errorbar(bv, vk, xerr=bverr, yerr=vkerr,lolims=upperlimit, ls='none', capsize=3, elinewidth=2, mew=2, barsabove=True)
xlabel('$B-V$')
ylabel(r'$V-K_\textrm{\small s}$')
savefig('color_bv_vk.pdf')