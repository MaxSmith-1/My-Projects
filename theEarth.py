# SPICE - important package for space science


import numpy as np
import matplotlib.pyplot as plt
import math

import spiceypy

import datetime

today = datetime.datetime.today()

#todays date
todayStr = today.strftime("2021-09-22T00:00:00");

print(todayStr)

#SPICE reqires time in a certain format: ephemerist time

#loading kernels
spiceypy.furnsh("./kernels/lsk/naif0012.tls")
spiceypy.furnsh("./kernels/spk/de432s.bsp")

#emphemerist time: miliseconds since certain date
midnight = spiceypy.utc2et(todayStr)
print(midnight)


#kernels predict future positions, give data torwards celestial bodies
#before doing anything with a planet, you have to load and furnish the appropriate kernels
#lsk - leapseconds


#we are gonna try to find the speed of earth at "midnight" time
#NAIF ID codes: every celestial body/spacecraft has ID in spiceypy
#ref -> reference plane

#Compute state vector of the Earth with the Sun
#State vector - in this case, vector from earth to Sun -> Orgin is the Sun
#State vector has 6 arguments, 3 for position and 3 for velocity
#Codes:
#Earth = 399
#Sun = 10
#SSB = 0
earth_state_wrt_sun, earth_sun_light_time = spiceypy.spkgeo(targ=399,et=midnight,ref="ECLIPJ2000", obs=10)


print(earth_state_wrt_sun)
distance = math.sqrt(earth_state_wrt_sun[0] **2 + earth_state_wrt_sun[1]**2 + earth_state_wrt_sun[2]**2)
print(distance)

velocity = math.sqrt(earth_state_wrt_sun[3] **2 + earth_state_wrt_sun[4]**2 + earth_state_wrt_sun[5]**2)
print(velocity)
AUDistance = spiceypy.convrt(distance, "km", "au")
print(AUDistance)

#More on reference frames
#ECLIPJ2000 = ecliptic plane = coordinate plane
# X = pointing torwards sun during spring
# Y = tangent to orbit
# Z = comes out of plane
#System is steady for all times of the year



earth_position_wrt_sun = earth_state_wrt_sun[:3]

#normal position vector
earth_position_wrt_sun_normed = earth_position_wrt_sun / distance

earth_position_autumn = np.array([1.0,0.0,0.0])

degree_difference = np.degrees(np.arccos(np.dot(earth_position_wrt_sun_normed, earth_position_autumn)))

print(degree_difference)