n = int(input())
info = []
result = [1] * n

for _ in range(n):
    a, b = map(int, input().split())
    info.append((a, b))

for i in range(n-1):
    for j in range(i+1, n):
        if info[i][0] > info[j][0] and info[i][1] > info[j][1]:
            result[j] += 1
        elif info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            result[i] += 1

for i in result:
    print(i, end=" ")
