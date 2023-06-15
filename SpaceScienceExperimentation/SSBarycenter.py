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

initialTime = datetime.datetime(year=2000, month=1, day=1)
timePeriod = 10001
endTime = initialTime + datetime.timedelta(timePeriod)

initialTimeStr = initialTime.strftime('%Y-%m-%dT%H:%M:%S')
endTimeStr = endTime.strftime('%Y-%m-%dT%H:%M:%S')

initialTimeEt = spiceypy.utc2et(initialTimeStr)
endTimeEt = spiceypy.utc2et(endTimeStr)



sunPosition = []
sunPositionNormal = []

timeInterval = np.linspace(initialTimeEt, endTimeEt, timePeriod)

for i in timeInterval:
    position, _ = spiceypy.spkgps(targ=0, et=i, ref="ECLIPJ2000", obs=10)

    sunPosition.append(position)

#normalizing?
_, radii_sun = spiceypy.bodvcd(bodyid=10, item='RADII', maxn=3)

sunRadius = radii_sun[0]

sunPositionNormal = sunPosition / sunRadius

sunPositionNormalXY = sunPositionNormal[:,0:2]



plt.style.use("dark_background")

fig, ax = plt.subplots(figsize=(12,12))


sun = plt.Circle((0.0,0.0), 1, color="yellow", alpha=.6)
ax.add_artist(sun)

ax.plot(sunPositionNormalXY[:, 0], sunPositionNormalXY[:, 1], linestyle='solid', color='orange', alpha=1)
plt.plot(sunPositionNormalXY[0,0], sunPositionNormalXY[0,1], 'go')
plt.plot(sunPositionNormalXY[-1,0], sunPositionNormalXY[-1,1], 'ro')

ax.set_aspect("equal")
ax.grid(True, linestyle="dashed",alpha=.4)
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)


ssb_wrt_sun_distance_scaled = np.linalg.norm(sunPositionNormal,
                                             axis=1)

print('computation time: %s days\n' % timePeriod)

# Compute number of days outside the Sun
ssb_outside_sun_delta_days = len(np.where(ssb_wrt_sun_distance_scaled > 1)[0])

print('fraction of time where the ssb\n' 
      'was outside the sun: %s %%' % (100 * ssb_outside_sun_delta_days
                                      / timePeriod))

plt.show()

# How many days is the SSB outside the Sun? First, we compute the euclidean
# distance between the SSB and Sun.



