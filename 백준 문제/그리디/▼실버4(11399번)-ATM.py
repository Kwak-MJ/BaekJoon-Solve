n = int(input())
time = list(map(int, input().split()))

time.sort(reverse=True)

result = 0
for i in range(1, n+1):
    result += i * time[i-1]

print(result)
