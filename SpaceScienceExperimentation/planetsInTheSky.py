import pandas as pd
import spiceypy
import numpy as np
import datetime
from matplotlib import pyplot as plt


spiceypy.furnsh("./kernels/lsk/naif0012.tls")
spiceypy.furnsh("./kernels/spk/de432s.bsp")
spiceypy.furnsh("./kernels/pck/gm_de431.tpc")
spiceypy.furnsh("./kernels/pck/pck00010.tpc")

initialTime = datetime.datetime(year=2021, month=10, day=1)
timePeriod = 400
endTime = initialTime + datetime.timedelta(timePeriod)

initialTimeStr = initialTime.strftime('%Y-%m-%dT %H:%M:%S')
endTimeStr = endTime.strftime('%Y-%m-%dT %H:%M:%S')

initialTimeEt = spiceypy.utc2et(initialTimeStr)
endTimeEt = spiceypy.utc2et(endTimeStr)

timeInterval = np.linspace(initialTimeEt, endTimeEt, timePeriod)

innerSolarSystemDataFrame = pd.DataFrame()

innerSolarSystemDataFrame.loc[:, 'ET'] = timeInterval
innerSolarSystemDataFrame.loc[:, 'UTC'] = innerSolarSystemDataFrame['ET'].apply(lambda x: spiceypy.et2datetime(et=x))

#Computer angular distance between sun and earth
#Phase Angle = angle between 2 bodies
innerSolarSystemDataFrame.loc[:, 'Venus-Sun-Angle'] = innerSolarSystemDataFrame['ET'].apply(lambda x: np.degrees(spiceypy.phaseq(et=x, target='399', illmn='10', obsrvr='299', abcorr='LT+S')))
innerSolarSystemDataFrame.loc[:, 'Moon-Sun-Angle'] = innerSolarSystemDataFrame['ET'].apply(lambda x: np.degrees(spiceypy.phaseq(et=x, target='399', illmn='10', obsrvr='301', abcorr='LT+S')))
innerSolarSystemDataFrame.loc[:, 'Moon-Venus-Angle'] = innerSolarSystemDataFrame['ET'].apply(lambda x: np.degrees(spiceypy.phaseq(et=x, target='399', illmn='301', obsrvr='299', abcorr='LT+S')))

innerSolarSystemDataFrame.loc[:,"Photogenic"] = innerSolarSystemDataFrame.apply(lambda x: True if x['Venus-Sun-Angle'] > 30 and x['Moon-Sun-Angle'] > 30 and x['Moon-Venus-Angle'] < 10.0 else False, axis = 1)


count = 0



plt.style.use("dark_background")

fig, ax = plt.subplots(figsize=(20,10))


ax.plot(innerSolarSystemDataFrame['UTC'], innerSolarSystemDataFrame["Venus-Sun-Angle"], color='orange',label="Venus-Sun")

ax.plot(innerSolarSystemDataFrame['UTC'], innerSolarSystemDataFrame["Moon-Sun-Angle"], color='grey',label="Moon-Sun")

ax.plot(innerSolarSystemDataFrame['UTC'], innerSolarSystemDataFrame["Moon-Venus-Angle"], color='yellow',label="Venus-Moon")




ax.grid(axis='x', linestyle="dashed", color="pink")
ax.set_xlabel("Dates in UTC")
ax.set_ylabel("Angles in Degrees")

count = 0
for i in innerSolarSystemDataFrame['Photogenic']:
    count+=1
    if i:
        ax.plot(innerSolarSystemDataFrame['UTC'].values[count], i, 'go')



plt.show()
