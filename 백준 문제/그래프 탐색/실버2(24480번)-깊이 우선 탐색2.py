import sys
sys.setrecursionlimit(10**5)


def dfs(current: int, count: int):  # dfs 함수는 visited=0인게 보장된 상태에서 실행함, global 변수 써도 쉽게 가능
    visited[current] = count
    for i in sorted(group[current], reverse=True):
        if visited[i] == 0:
            count += 1
            count = dfs(i, count)
    return count


n, m, u = map(int, sys.stdin.readline().split())
group = [[] for _ in range(n+1)]
visited = [0] * (n+1)
c = 1

for _ in range(m):
    v, w = map(int, sys.stdin.readline().split())
    group[v].append(w)
    group[w].append(v)

dummy = dfs(u, 1)
for i in visited[1:]:
    print(i)
