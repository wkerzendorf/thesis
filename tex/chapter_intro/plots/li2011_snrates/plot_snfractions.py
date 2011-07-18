execfile('../../../thesis_plot_defaults.py')

all_fracs = [4, 79, 17]
ia_fracs = [2, 18, 3, 77]
ibc_fracs = [32, 15, 52]
ii_fracs = [29, 17, 25, 30]

all_labels = [r'Ib/c (4\,\%)', r'Ia (79\,\%)', r'II (17\,\%)']
ia_labels = [r'02cx (2\,\%)', r'91T (18\,\%)', r'91bg (3\,\%)', r'Normal (77\,\%)']
ibc_labels = [r'Ib (32\,\%)', r'Ibc-pec (15\,\%)', r'Ic (52\,\%)']
ii_labels = [r'IIn (29\,\%)', r'IIb (17\,\%)', r'II-L (25\,\%)', r'II-P (30\,\%)']


clf()
fig=pylab.figure(1, figsize=(8,8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

pie(all_fracs, labels=all_labels, shadow=True)
savefig('../plot_all_fracs.pdf')

fig.clf()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
pie(ia_fracs, labels=ia_labels, shadow=True)
savefig('../plot_ia_fracs.pdf')

fig.clf()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
pie(ibc_fracs, labels=ibc_labels, shadow=True)
savefig('../plot_ibc_fracs.pdf')

fig.clf()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
pie(ii_fracs, labels=ii_labels, shadow=True)
savefig('../plot_ii_fracs.pdf')

