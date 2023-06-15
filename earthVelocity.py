import math

import spiceypy
import numpy as np;

import datetime


spiceypy.furnsh("./kernels/pck/gm_de431.tpc")

x, GM = spiceypy.spiceypy.bodvcd(bodyid=10, item="GM", maxn=1)



orbital_function = lambda gn, r: np.sqrt(gn/r)


earth_orbidal_speed = orbital_function(GM[0], 150162351.28708932)

print(earth_orbidal_speed)
print(math.sqrt(GM/150162351.28708932))