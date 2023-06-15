import math

import spiceypy
import numpy as np
import datetime
import pandas as pd
from matplotlib import pyplot as plt


spiceypy.furnsh("./kernels/lsk/naif0012.tls")
spiceypy.furnsh("./kernels/spk/de432s.bsp")
spiceypy.furnsh("./kernels/pck/gm_de431.tpc")
spiceypy.furnsh("./kernels/pck/pck00010.tpc")

#Date Stuff
initialTime = datetime.datetime(year=2001, month=1, day=1)
timePeriod = 10001
endTime = initialTime + datetime.timedelta(timePeriod)

initialTimeStr = initialTime.strftime('%Y-%m-%dT%H:%M:%S')
endTimeStr = endTime.strftime('%Y-%m-%dT%H:%M:%S')

#converts utc date to ephemerist date
initialTimeEt = spiceypy.utc2et(initialTimeStr)
endTimeEt = spiceypy.utc2et(endTimeStr)

timeInterval = np.linspace(initialTimeEt, endTimeEt, timePeriod)

#Spiceypy method to compute radius of sun
_, radii_sun = spiceypy.bodvcd(bodyid=10, item='RADII', maxn=3)

sunRadius = radii_sun[0]

#Computing Phase Angle between objects
#Phase Angle - Angle between vector from center of sun to barycenter and center of sun to an object


#Makes pandas data frame with times, Pos of SSB,
solarSystemDataFrame = pd.DataFrame()

solarSystemDataFrame.loc[:,"ET"] = timeInterval
solarSystemDataFrame.loc[:,"UTC"] = solarSystemDataFrame["ET"].apply(lambda x: spiceypy.et2datetime(et=x).date())
solarSystemDataFrame.loc[:, "Pos. SSB"] = solarSystemDataFrame["ET"].apply(lambda x: spiceypy.spkgps(targ=0, et=x, ref="ECLIPJ2000", obs=10)[0])
solarSystemDataFrame.loc[:,"Scaled Pos"] = solarSystemDataFrame["Pos. SSB"].apply(lambda x: x / sunRadius)
solarSystemDataFrame.loc[:, "Scaled Distance"] = solarSystemDataFrame["Scaled Pos"].apply(lambda x: math.sqrt(x[0]**2 + x[1]**2 + x[2]**2))



#Compute Phase Angle of planets
#Jupuiter = 5
#Saturn = 6

solarSystemDataFrame.loc[:,"JupiterPos"] = solarSystemDataFrame["ET"].apply(lambda x: spiceypy.spkgps(targ=5, et=x , ref="ECLIPJ2000", obs=10)[0])
solarSystemDataFrame.loc[:,"JupiterScaled Pos"] = solarSystemDataFrame["JupiterPos"].apply(lambda x: x / sunRadius)


solarSystemDataFrame.loc[:, "PlanetAngle"] = solarSystemDataFrame.apply(lambda x: np.degrees(spiceypy.vsep(x["JupiterPos"], x["Pos. SSB"])), axis=1)
print(solarSystemDataFrame)


#Graphing all this stuff: change in barycenter with respect to Phase Angle of Each Planet
#Create a way to do it for all planets

plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(12,12))

#Potential for loop here

plt.title("Distance Between Center of Sun and Solar System Barycenter", color="pink")
ax.plot(solarSystemDataFrame["UTC"], solarSystemDataFrame["Scaled Distance"], color="blue")
plt.axhline(y = 1.0, color = 'r', linestyle = '-')

axAdditional = ax.twinx()

axAdditional.plot(solarSystemDataFrame["UTC"], solarSystemDataFrame["PlanetAngle"], color="green")


ax
plt.show()