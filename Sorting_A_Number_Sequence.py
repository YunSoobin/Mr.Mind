import numpy as np
import random
import pickle
from collections import Counter

MAX_NUM = 65535
all_num = 1000000
memory_limit = 100000


print("Memory Limit :", memory_limit)


# A : 16 bit unsigned integer 1,000,000개 hexDec.bin 파일에 저장
with open("hexDec.bin", "ab+") as fp:
    for i in range(all_num):
        randomNum = np.uint16(random.randint(0, MAX_NUM))
        pickle.dump(randomNum, fp)


# # hexDec.bin 파일 출력
# print("=== hexDec.bin ===")
#
# showresult = []
# with open("hexDec.bin", "rb") as fr:
#     try:
#         while True:
#             showresult.append(pickle.load(fr))
#     except EOFError:
#         pass
#
# print(showresult)
# print("hexDec result len :",len(showresult))
# del showresult



# B : hexDec.bin 파일에 저장된 숫자 오름차순 정렬하여 hexDecSort.bin 파일에 저장
# Count Sort
count = [0] * memory_limit  # MAX_NUM + 1(= 65535 + 1) size만 사용

with open("hexDec.bin", "rb") as fr:
    try:
        while True:
            count[pickle.load(fr)] += 1  # 각 데이터에 해당하는 인덱스의 값 증가
    except EOFError:
        pass


with open("hexDecSort.bin", "ab+") as fp:
    for i in range(MAX_NUM + 1):
        if count[i] != 0:
            for _ in range(count[i]):
                pickle.dump(i, fp)


# # hexDecSort.bin 파일 출력
# print("=== hexDecSort.bin ===")
#
# showresult = []
# with open("hexDecSort.bin", "rb") as fr:
#     try:
#         while True:
#             showresult.append(pickle.load(fr))
#     except EOFError:
#         pass
#
# print(showresult)
# print("hexSortDec result len :",len(showresult))
# del showresult



# C : hexDecSort.bin 파일에 저장된 숫자 빈도수 기준 오름차순 정렬하여 hexDecSizeSort.bin 파일에 저장
countSort = {number : numbercount for number, numbercount in enumerate(count)}
countSort = Counter(countSort).most_common()

with open("hexDecSizeSort.bin", "ab+") as fp:
    for i in range(MAX_NUM + 1):
        if countSort[i][1] != 0:
            for _ in range(countSort[i][1]):
                pickle.dump(countSort[i][0], fp)


# # hexDecSizeSort.bin 파일 출력
# print("=== hexDecSizeSort.bin ===")
#
# showresult = []
# with open("hexDecSizeSort.bin", "rb") as fr:
#     try:
#         while True:
#             showresult.append(pickle.load(fr))
#     except EOFError:
#         pass
#
# print(showresult)
# print("hexDecSizeSort result len :",len(showresult))
# del showresult
