# solved.ac 레이팅 골드5 97점, 실버1 -7점
from collections import deque
n = int(input())
group = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(i: int, j: int, house: int):
    global complex
    que = deque()
    group[i][j] = 10
    que.append((i, j))
    complex += 1

    while que:
        x, y = que.popleft()
        house += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if group[nx][ny] == 1:
                    group[nx][ny] = 10
                    que.append((nx, ny))

    return house


for _ in range(n):
    group.append(list(map(int, list(input()))))

result = []
complex = 0
for i in range(n):
    for j in range(n):
        house = 0
        if group[i][j] == 1:
            result.append(bfs(i, j, house))

print(complex)
for i in sorted(result):
    print(i)
