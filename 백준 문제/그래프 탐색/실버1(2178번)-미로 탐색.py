from collections import deque
n, m = map(int, input().split())
graph = []
visited = [[0]*m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, list(input()))))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

sx = 0
sy = 0
q = deque()
q.append((sx, sy))
visited[sx][sy] = 1

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

print(visited[n-1][m-1])
