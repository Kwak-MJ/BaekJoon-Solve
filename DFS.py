# 일반적인 무방향 dfs 에서는 인접 정점을 오름차순으로 탐색
import sys

c = 1


def dfs(r):
    global c
    visited[r] = c
    graph[r].sort()
    for i in graph[r]:
        if visited[i] == 0:
            c += 1
            dfs(i)


sys.setrecursionlimit(200000)
n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


dfs(r)

for i in visited[1:]:
    print(i)
