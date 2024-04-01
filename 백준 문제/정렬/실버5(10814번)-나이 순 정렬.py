n = int(input())
result = []
for _ in range(n):
    age, name = input().split()
    result.append([int(age), name])

result.sort(key=lambda x: x[0])

for j in result:
    print(j[0], j[1])
