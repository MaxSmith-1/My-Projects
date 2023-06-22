#sky map
#Ecliptic Coordinates - sky seen from earth
#In this project, we are going to graph the motion of celestial objects in the night sky as seen from earth using spice




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

y=2000
m=10
d=10


def refresh(timePeriod):

    initialTime = datetime.datetime(year=y, month=m, day=d)

    endTime = initialTime + datetime.timedelta(timePeriod)

    initialTimeStr = initialTime.strftime('%Y-%m-%dT%H:%M:%S')
    endTimeStr = endTime.strftime('%Y-%m-%dT%H:%M:%S')

    initialTimeEt = spiceypy.utc2et(initialTimeStr)
    endTimeEt = spiceypy.utc2et(endTimeStr)


    timeInterval = np.linspace(initialTimeEt, endTimeEt, timePeriod)




    #Correction??
    #Scaled to AU

    solarSystemObjects = pd.DataFrame()

    solarSystemObjects.loc[:, 'ET'] = timeInterval
    solarSystemObjects.loc[:, 'UTC'] = solarSystemObjects['ET'].apply(lambda x: spiceypy.et2datetime(et=x))



    objects = {"Sun" : 10, "Venus": 299, "Moon": 301, "Mars": 4}

    colors = ['yellow', 'orange', 'white', 'red']
    count = 0
    for i in objects:

        solarSystemObjects.loc[:, i] = solarSystemObjects['ET'].apply(lambda x: spiceypy.spkgps(targ=objects[i], et=x, ref="ECLIPJ2000", obs=399)[0] / 149600000)

        #recrad = converts x,y,z vectors into coordinates 1+longitude 2=ladutide
        solarSystemObjects.loc[:, f'{i}EC_CoordinatesLong'] = solarSystemObjects[i].apply(lambda x: spiceypy.recrad(x)[1])

        solarSystemObjects.loc[:, f'{i}EC_CoordinatesLad'] = solarSystemObjects[i].apply(lambda x: spiceypy.recrad(x)[2])

    return solarSystemObjects



def graph():
    objects = {"Sun": 10, "Venus": 299, "Moon": 301, "Mars": 4}
    colors = ['yellow', 'orange', 'white', 'red']
    count = 0
    timePeriod = 200
    ssolarSystemObjects = refresh(timePeriod)

    plt.style.use("dark_background")

    plt.figure(figsize=(12,12))

    plt.subplot(projection="aitoff")
    plt.grid(True)

    plt.xticks(ticks=np.radians([-150, -120, -90, -60, -30, 0,
                                 30, 60, 90, 120, 150]),
               labels=['150°', '120°', '90°', '60°', '30°', '0°',
                       '330°', '300°', '270°', '240°', '210°'])



    for i in objects:
        plt.plot(ssolarSystemObjects[f'{i}EC_CoordinatesLong'].iloc[0], ssolarSystemObjects[f'{i}EC_CoordinatesLad'].iloc[0],
                 'go', alpha=.9)
        plt.plot(ssolarSystemObjects[f'{i}EC_CoordinatesLong'], ssolarSystemObjects[f'{i}EC_CoordinatesLad'], color=colors[count], alpha = .9)
        plt.plot(ssolarSystemObjects[f'{i}EC_CoordinatesLong'].iloc[-1], ssolarSystemObjects[f'{i}EC_CoordinatesLad'].iloc[-1],
                 'ro', alpha=.9)
        count += 1

    plt.subplots_adjust(bottom=.25)
    sliderA = plt.axes([0.1, 0.1, .8, .05])
    sliderVal = Slider(sliderA, "Days Since " + datetime.datetime(year=y, month=m, day=d).strftime('%Y-%m-%d'),
                       valmin=0, valmax=timePeriod, valinit=timePeriod, valstep=1, closedmin=False)
    # onchanged



    # Set the axes labels
    plt.xlabel('Eclip. long. in deg')
    plt.ylabel('Eclip. lat. in deg')

    # Create a legend and grid

    plt.grid(True)

    # Save the figure
    plt.savefig('eclipj2000_sky_map.png', dpi=300)







    plt.show()

graph()