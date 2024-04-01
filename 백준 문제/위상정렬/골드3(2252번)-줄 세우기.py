import sys
input = sys.stdin.readline
n, m = map(int, input().split())
l = [[] for _ in range(n+1)]
cnt = [0]*(n+1)
ans = []

for i in range(m):
    a, b = map(int, input().split())
    l[a].append(b)
    cnt[b] += 1

flag = n
q = []
for i in range(1, n + 1):
    if cnt[i] == 0:
        q.append(i)
while len(q):
    i = q.pop()
    ans.append(str(i))
    for j in l[i]:
        cnt[j] -= 1
        if cnt[j] == 0:
            q.append(j)

print(' '.join(ans))
