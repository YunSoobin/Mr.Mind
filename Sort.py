numbers = list(map(int, input("공백으로 구분하여 숫자를 입력하세요. : ").split()))

allCount = len(numbers)   # 숫자 개수
evenCount = 0   # 짝수 개수
oddCount = 0    # 홀수 개수

for i in numbers:
    if i % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1

i = 0
j = allCount - 1
while True:
    if i >= j:
        break

    if numbers[i] % 2 == 0:
        i += 1
        if numbers[j] % 2 == 1:
            j -= 1
    else:
        if numbers[j] % 2 == 0:
            numbers[i], numbers[j] = numbers[j], numbers[i] # 짝수는 왼쪽으로, 홀수는 오른쪽으로 swap
            i += 1
            j -= 1
        else:
            j -= 1

numbers = sorted(numbers[:evenCount], reverse=True) + sorted(numbers[evenCount:], reverse=True) # 짝수, 홀수 각각 정렬하여 병합
print(numbers)