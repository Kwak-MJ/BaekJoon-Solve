n = int(input())

table = []

for _ in range(n):
    start, end = map(int, input().split())
    table.append((start, end))

table = sorted(table, key=lambda x: (x[1], x[0]))


last_end = 0
tmp = 0

for start, end in table:
    if start >= last_end:
        tmp += 1
        last_end = end

print(tmp)
