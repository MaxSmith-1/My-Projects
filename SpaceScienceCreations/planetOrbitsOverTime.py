#Center of the Solar System is not the sun: everything contributes gravity, which changes the center


#Distance between barycenter and sun
#Time dependent

import spiceypy
import numpy as np
import datetime
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

#Kerels are furnished, we have the information needed to pull data from spice
spiceypy.furnsh("./kernels/lsk/naif0012.tls")
spiceypy.furnsh("./kernels/spk/de432s.bsp")
spiceypy.furnsh("./kernels/pck/gm_de431.tpc")
spiceypy.furnsh("./kernels/pck/pck00010.tpc")





def orbitGraph(y, m, d, tD, planetId):

    initialTime = datetime.datetime(year=y, month=m, day=d)
    timePeriod = tD
    endTime = initialTime + datetime.timedelta(timePeriod)

    initialTimeStr = initialTime.strftime('%Y-%m-%dT%H:%M:%S')
    endTimeStr = endTime.strftime('%Y-%m-%dT%H:%M:%S')

    initialTimeEt = spiceypy.utc2et(initialTimeStr)
    endTimeEt = spiceypy.utc2et(endTimeStr)
    pos = []

    timeInterval = np.linspace(initialTimeEt, endTimeEt, timePeriod)


    for i in timeInterval:
        position, _ = spiceypy.spkgps(targ=planetId, et=i, ref="ECLIPJ2000", obs=10)

        pos.append(position)

    #normalizing?
    _, oR = spiceypy.bodvcd(bodyid=10, item='RADII', maxn=3)

    orbitRadius = oR[0]

    scaledPos = pos / orbitRadius

    scaledPosXY = scaledPos[:,0:2]

    return scaledPosXY


def graph(y,m,d,tD,r):

    if r<=6:
        a=3000
    else:
        a=6000

    orbitColors = ["", "yellow", "orange", "blue", "red", "orange", "yellow", "blue", "blue"]
    plt.style.use("dark_background")

    fig, ax = plt.subplots(figsize=(12,12))


    sun = plt.Circle((0.0,0.0), 1, color="yellow", alpha=.6)
    ax.add_artist(sun)

    for i in range(r):
        if i!=0:
            ax.plot(orbitGraph(y,m,d,tD,i)[:, 0], orbitGraph(y,m,d,tD,i)[:, 1], linestyle='solid', color=orbitColors[i], alpha=1)
            plt.plot(orbitGraph(y,m,d,tD,i)[0,0], orbitGraph(y,m,d,tD,i)[0,1], 'go')
            plt.plot(orbitGraph(y,m,d,tD,i)[-1,0], orbitGraph(y,m,d,tD,i)[-1,1], 'ro')

    ax.set_aspect("equal")
    ax.grid(True, linestyle="dashed",alpha=.4)
    ax.set_xlabel("Distance from Sun (1 unit = 69600 km)")
    ax.set_ylabel("Distance from Sun (1 unit = 69600 km)")
    ax.set_xlim(-a,a)
    ax.set_ylim(-a,a)

    #When we have a slider, we are changing the TD value

    plt.subplots_adjust(bottom =.25)
    sliderA = plt.axes([0.1,0.1,.8,.05])

    sliderVal = Slider(sliderA, "Days Since ", valmin=0, valmax=tD, valinit=tD, valstep=1, closedmin=False)

    #onchanged

    def updateValue(val):
        ax.clear()
        for i in range(r):
            if i != 0:
                ax.plot(orbitGraph(y, m, d, sliderVal.val, i)[:, 0], orbitGraph(y, m, d, sliderVal.val, i)[:, 1], linestyle='solid',
                        color=orbitColors[i], alpha=1)

        ax.set_aspect("equal")
        ax.grid(True, linestyle="dashed", alpha=.4)
        ax.set_xlabel("Distance from Sun (1 unit = 69600 km)")
        ax.set_ylabel("Distance from Sun (1 unit = 69600 km)")
        ax.set_xlim(-a, a)
        ax.set_ylim(-a, a)

    sliderVal.on_changed(updateValue)
    plt.show()

   

graph(2023,1,1,365,6)



