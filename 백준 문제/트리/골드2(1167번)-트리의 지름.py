import sys
from collections import deque
sys.setrecursionlimit(200000)

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n):
    A = list(map(int, input().split()))
    u = A[0]
    A = A[1:]

    i, j = 0, 1
    while A[i] != -1:
        v, w = A[i], A[j]
        graph[u].append((w, v))

        i += 2
        j += 2


def dfs(node: int, tmp: int):
    for w, v in graph[node]:
        if distance[v] == -1:
            distance[v] = tmp + w
            dfs(v, tmp + w)


distance = [-1] * (n+1)
distance[1] = 0
dfs(1, 0)
start = distance.index(max(distance))

distance = [-1] * (n+1)
distance[start] = 0
dfs(start, 0)
print(max(distance))
