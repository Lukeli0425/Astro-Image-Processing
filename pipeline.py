import numpy as np
from astropy.io import fits
import glob

sources = ['TOI-5278']
path = '/Users/luke/Desktop/Project2/data/20220513_80/'
for s in sources:
    fnn = sorted(glob.glob(path + s + '*.fits'))
    for i in fnn:
        print(i)
        aaa = fits.open(i,mode='update')
        aaa.headers()
        # fits.setval(i,keyword='CDELT1',value=0.388*2/3600)
        # fits.setval(i,keyword='CDELT2',value=0.388*2/3600)
        # angle = fits.getval(i,keyword='ANGLE')
        # angle_rad = np.deg2rad(angle)
        # fits.setval(i,keyword='CROTA2',value=angle_rad)
        # CD1_1 = 0.388*2/3600 * np.cos(angle_rad)
        # CD1_2 = -0.388*2/3600 * np.sin(angle_rad)
        # CD2_1 = 0.388*2/3600 * np.sin(angle_rad)
        # CD2_2 = 0.388*2/3600 * np.cos(angle_rad)
        # fits.setval(i,keyword='CD1_1',value=CD1_1)
        # fits.setval(i,keyword='CD1_2',value=CD1_2)
        # fits.setval(i,keyword='CD2_1',value=CD2_1)
        # fits.setval(i,keyword='CD2_2',value=CD2_2)
        aaa.close()
        
