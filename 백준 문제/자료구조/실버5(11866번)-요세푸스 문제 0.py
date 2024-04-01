# 요세푸스 문제는 deque의 rotate를 이용하면 간단함
n, k = map(int, input().split())
nums = list(range(1, n+1))

pointer = -1
result = []

while nums:
    pointer += k

    while pointer >= len(nums):
        pointer -= len(nums)

    result.append(nums[pointer])
    del nums[pointer]

    pointer -= 1

print('<', end='')
for i in range(len(result)):
    print(result[i], end='')

    if len(result) == 1:
        break
    if i != len(result)-1:
        print(', ', end='')
print('>', end='')
