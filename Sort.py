numbers = list(map(int, input("공백으로 구분하여 숫자를 입력하세요. : ").split()))

allCount = len(numbers)   # 숫자 개수
evenCount = 0   # 짝수 개수
oddCount = 0    # 홀수 개수

for i in numbers:
    if i % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1

i = 0   # 왼쪽부터 정렬
j = allCount - 1    # 오른쪽부터 정렬
while True:
    if i >= j:
        break

    # 왼쪽에 짝수, 오른쪽에 홀수가 존재하여 swap할 필요가 없는 경우
    if numbers[i] % 2 == 0:
        i += 1
        if numbers[j] % 2 == 1:
            j -= 1
    else:
        # 왼쪽에 홀수, 오른쪽에 짝수가 존재하여 swap해야 하는 경우
        if numbers[j] % 2 == 0:
            numbers[i], numbers[j] = numbers[j], numbers[i] # 짝수는 왼쪽으로, 홀수는 오른쪽으로 swap
            i += 1
            j -= 1
        else:
            j -= 1

numbers = sorted(numbers[:evenCount], reverse=True) + sorted(numbers[evenCount:], reverse=True) # 짝수, 홀수 각각 내림차순 정렬하여 병합
print(numbers)