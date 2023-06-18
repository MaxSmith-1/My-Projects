#sky map
#Ecliptic Coordinate -




import spiceypy
import numpy as np
import datetime
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

spiceypy.furnsh("./kernels/lsk/naif0012.tls")
spiceypy.furnsh("./kernels/spk/de432s.bsp")
spiceypy.furnsh("./kernels/pck/gm_de431.tpc")
spiceypy.furnsh("./kernels/pck/pck00010.tpc")


todayUTC = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

todayET = spiceypy.utc2et(todayUTC)


solarSystemObjects = pd.DataFrame()

solarSystemObjects.loc[:, 'ET'] = [todayET]

solarSystemObjects.loc[:, 'UTC'] = [todayUTC]

objects = {"Sun" : 10, "Venus": 299, "Moon": 301, "Mars": 4}

#Correction??
#Scaled to AU
for i in objects:
    solarSystemObjects.loc[:, i] = solarSystemObjects['ET'].apply(lambda x: spiceypy.spkgps(targ=objects[i], et=x, ref="ECLIPJ2000", obs=399)[0] / 149600000)

    #recrad = converts x,y,z vectors into coordinates 1+longitude 2=ladutide
    solarSystemObjects.loc[:, f'{i}EC_CoordinatesLong'] = solarSystemObjects[i].apply(lambda x: spiceypy.recrad(x)[1])

    solarSystemObjects.loc[:, f'{i}EC_CoordinatesLad'] = solarSystemObjects[i].apply(lambda x: spiceypy.recrad(x)[2])




plt.style.use("dark_background")

plt.figure(figsize=(10,10))

plt.subplot(projection="aitoff")
plt.grid(True)


colors = ['y', 'y', 'w', 'r']
count = 0
for i in objects:
    plt.plot(solarSystemObjects[f'{i}EC_CoordinatesLong'], solarSystemObjects[f'{i}EC_CoordinatesLad'], f'{colors[count]}o', alpha = .9)
    count +=1

plt.xticks(ticks=np.radians([-150, -120, -90, -60, -30, 0, \
                             30, 60, 90, 120, 150]),
           labels=['150°', '120°', '90°', '60°', '30°', '0°', \
                   '330°', '300°', '270°', '240°', '210°'])

# Set the axes labels
plt.xlabel('Eclip. long. in deg')
plt.ylabel('Eclip. lat. in deg')

# Create a legend and grid

plt.grid(True)

# Save the figure
plt.savefig('eclipj2000_sky_map.png', dpi=300)

plt.show()