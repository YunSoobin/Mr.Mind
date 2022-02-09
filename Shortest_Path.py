import math
import numpy as np

minTime = 100   # D에 도착하는 최소 시간
minI = 0
for i in np.arange(0, 25, 0.01):
    XZoneTime = math.sqrt(pow(10, 2) + pow(i, 2)) / 1
    YZoneTime = math.sqrt(pow(10, 2) + pow((25- i),2)) / 2
    time = XZoneTime + YZoneTime

    if time < minTime:
        minTime = time
        minI = i

XZonePath = math.sqrt(pow(10, 2) + pow(minI, 2))
YZonePath = math.sqrt(pow(10, 2) + pow((25- minI),2))

print(XZonePath + YZonePath,"m")