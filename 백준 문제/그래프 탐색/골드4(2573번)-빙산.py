from collections import deque
n, m = map(int, input().split())
graph = []

notzero = 0
for _ in range(n):
    insert = list(map(int, input().split()))
    graph.append(insert)
    notzero += m - insert.count(0)


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
day = 0


def bfs(i: int, j: int):
    visited2[i][j] = 1
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited2[nx][ny] == 0 and graph[nx][ny] != 0:
                    visited2[nx][ny] = 1
                    q.append((nx, ny))
    return 1


while notzero:
    day += 1
    visited = [[0]*m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if graph[i][j] != 0:
                visited[i][j] = day
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < n and 0 <= nj < m:
                        if visited[ni][nj] == 0 and graph[ni][nj] == 0:
                            graph[i][j] -= 1
                            if graph[i][j] == 0:
                                notzero -= 1

                if graph[i][j] < 0:
                    graph[i][j] = 0

    # 여기서 bfs 실행, 덩어리 파악하기
    visited2 = [[0]*m for _ in range(n)]
    group = 0
    for i in range(1, n):
        for j in range(1, m):
            if graph[i][j] != 0 and visited2[i][j] == 0:
                group += bfs(i, j)

    if group > 1:
        print(day)
        break

if group < 2:
    print(0)
