import sys
from collections import deque
# dfs
# import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
parent = [0]*(n+1)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(s):
    for i in graph[s]:
        if parent[i] == 0:
            parent[i] = s
            dfs(i)


dfs(1)
for i in range(2, n+1):
    print(parent[i])


# bfs
# import sys
# from collections import deque

N = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

ans = [0]*(N+1)


def bfs():
    while queue:
        current = queue.popleft()
        for child in graph[current]:
            if ans[child] == 0:
                ans[child] = current
                queue.append(child)


bfs()
res = ans[2:]
for x in res:
    print(x)
