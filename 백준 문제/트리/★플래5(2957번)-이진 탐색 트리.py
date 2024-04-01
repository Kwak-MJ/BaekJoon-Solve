import sys

N = int(sys.stdin.readline().rstrip())
di = [[i-1, i+1] if 0 < i < N+1 else [0, 0] for i in range(N+2)]
l = []
for i in range(N):
    l.append(int(sys.stdin.readline().rstrip()))
for i in l[::-1]:
    di[di[i][1]][0] = di[i][0]
    di[di[i][0]][1] = di[i][1]
k = [-1]+[0]*N+[-1]
ans = 0
for i in l:
    k[i] = max(k[di[i][0]], k[di[i][1]])+1
    ans += k[i]
    print(ans)
