from collections import deque
n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]


for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(start: int):
    visited[start] = True
    print(start, end=' ')
    for child in sorted(graph[start]):
        if visited[child] == False:
            dfs(child)


def bfs(start: int):
    visited[start] = True
    print(start, end=' ')
    q = deque()
    q.append(start)
    while q:
        v = q.popleft()
        for child in sorted(graph[v]):
            if visited[child] == False:
                visited[child] = True
                print(child, end=' ')
                q.append(child)


visited = [False] * (n+1)
dfs(start)
print()

visited = [False] * (n+1)
bfs(start)
