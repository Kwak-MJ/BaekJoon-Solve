n = input()
length = len(n)
result = 0

for i in range(9*length, -1, -1):
    if i > int(n):
        continue
    tmp = str(int(n) - i)
    count = 0
    for j in tmp:
        count += int(j)
    if count == i:
        result = int(tmp)
        break

print(result)
