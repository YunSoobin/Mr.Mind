# pond : 10 * 10 디지털 연못
pond =[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# 확인할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def depth(x, y):
    if pond[x][y] == 0:
        return False

    # 현재 위치에서 네 방향으로의 위치 확인
    min = pond[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if pond[nx][ny] < min:
            return False
    return True

while True:
    flag = False
    # 연못의 가장자리는 모두 땅(0)이기 때문에 확인 범위를 (1,10)으로 설정
    for i in range(1, 10):
        for j in range(1, 10):
            if depth(i, j) == True: # 상, 하, 좌, 우 모두가 자신보다 깊이가 같거나 큰 경우
                pond[i][j] += 1
                flag = True
    if flag == False:   # 더이상 물의 깊이가 증가할 수 없을 때 종료
        break

result = 0
for i in range(1, 10):
    for j in range(1, 10):
        result += pond[i][j]

print(result)