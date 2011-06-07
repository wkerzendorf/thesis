#load internal matplotlib defaults


rcdefaults()
defaultTextSize = 15

rc('xtick',labelsize=defaultTextSize,color='black')
rc('ytick',labelsize=defaultTextSize,color='black')
rc('font',weight='bold', size = defaultTextSize, family = 'serif')
rc('text', usetex = True)
rc('axes',labelsize = defaultTextSize)
rc('lines', linewidth = 2)
rc('figure', figsize = (8,6))