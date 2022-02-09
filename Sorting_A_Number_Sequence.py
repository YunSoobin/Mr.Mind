import random
import numpy as np
from collections import Counter

size = 100000
print("memory limit : ", size)

randomList = []

# a
for i in range(size):
    randomList.append(np.uint16(random.randint(0, 1000000)))

randomListSort = sorted(randomList) # b

# c
def frequency_sort(data):
	countSorted = []
	for d, c in Counter(data).most_common():
		for i in range(c):
			countSorted.append(d)
	return countSorted

randomListSizeSort = frequency_sort(randomList)

f = open("hexDec.bin", "w")
f.write('\n'.join(map(str, randomList)))
f.close()

f = open("hexDecSort.bin", "w")
f.write('\n'.join(map(str, randomListSort)))
f.close()

f = open("hexDecSizeSort.bin", "w")
f.write('\n'.join(map(str, randomListSizeSort)))
f.close()

