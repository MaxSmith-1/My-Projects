#Center of the Solar System is not the sun: everything contributes gravity, which changes the center


#Distance between barycenter and sun
#Time dependent

import spiceypy
import numpy as np
import datetime
from matplotlib import pyplot as plt


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
    ax.set_xlim(-500,500)
    ax.set_ylim(-500,500)



    plt.show()

    # How many days is the SSB outside the Sun? First, we compute the euclidean
    # distance between the SSB and Sun.

graph(2027,1,1,200,5)



