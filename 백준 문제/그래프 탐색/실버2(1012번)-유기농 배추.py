'''
1.아이디어
bfs로 풀어주면 될 것 같음

지렁이는 인접한 배추 전체 다 보호 가능

같이 붙어있는 군집의 수만 세면 됨

시간 줄이려면 1이 저장된 인덱스를 미리 알면 좋을듯?
(문제에서 주어지네, 쉬운문제임)

2. 시간 복잡도
결국 2500개 중 
최대 2500개 탐험 bfs 실행해야됨

bfs 는 O(v+e)

시간은 1초면 충분할듯

3. 예외 케이스
'''
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x: int, y: int):
    visited[y][x] = 0
    dq = [(x, y)]

    while dq:
        cur = dq.pop()
        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[ny][nx] == 1:
                    visited[ny][nx] = 0
                    dq.append((nx, ny))


test = int(input())

for _ in range(test):
    m, n, k = map(int, input().split())
    visited = [[0] * m for _ in range(n)]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        visited[y][x] = 1

    for j in range(n):
        for i in range(m):
            if visited[j][i] == 1:
                bfs(i, j)
                count += 1

    print(count)
