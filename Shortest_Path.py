import math
import numpy as np

INF = 999999999 # 무한의 비용 선언

minTime = INF   # D에 도착하는 최소 시간
minI = 0    # C(0,0), D(20,25)의 좌표 평면을 생성하였다고 가정,
            # 점 A는 minTime을 도출하는 X Zone과 Y Zone 경계선 위의 점,
            # minI는 점 A의 y좌표

for i in np.arange(0, 25, 0.0000001):
    CAlen = math.sqrt(pow(10, 2) + pow(i, 2))  # 점C와 점A 사이의 거리(m)
    DAlen = math.sqrt(pow(10, 2) + pow((25- i),2))  # 점D와 점A 사이의 거리(m)

    CAtime = CAlen / 1    # 점C에서 점A까지 걸리는 시간(min)
    DAtime =  DAlen / 2    # 점D에서 점A까지 걸리는 시간(min)
    time = CAtime + DAtime

    if time < minTime:
        minTime = time
        minI = i

minCAlen = math.sqrt(pow(10, 2) + pow(minI, 2)) # 점C와 점A 사이의 거리(m)
minDAlen = math.sqrt(pow(10, 2) + pow((25 - minI),2))   # 점D와 점A 사이의 거리(m)

print(minCAlen + minDAlen,"m")