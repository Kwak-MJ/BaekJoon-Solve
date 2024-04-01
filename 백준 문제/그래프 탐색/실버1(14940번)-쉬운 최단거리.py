'''
1. 아이디어
bfs()를 이용할꺼임
bfs 회차를 count 하여 visited 채우는 방식을 이용

visited 를 초깃값 -1로 채우기
graph에서 0 인 경우 visited도 0으로 바꾸기

bfs 실행하면 끝

2. 시간 복잡도
n = 1000, m = 1000
O(n*m) 도 가능

채점 결과 -> 7등 랭크
'''
import sys
from collections import deque

input = sys.stdin.readline

height, width = map(int, input().split())
visited = [[-1] * width for _ in range(height)]
graph = []
start = [0,0]

for i in range(height):
    insert_list = list(map(int, input().split()))
    for j in range(width):
        if insert_list[j] == 0:
            visited[i][j] = 0
        elif insert_list[j] == 2:
            start[0] = i
            start[1] = j
    graph.append(insert_list)

dh = [1, -1, 0, 0]
dw = [0, 0, 1, -1]

def bfs(h, w):
    count = 0
    dq = deque([[(h, w)]])
    visited[h][w] = count

    next = []
    while dq:
        group = dq.popleft()
        count += 1
        for ch, cw in group:
            for i in range(4):
                nh = ch + dh[i]
                nw = cw + dw[i]
                if 0 <= nh < height and 0 <= nw < width:
                    if visited[nh][nw] == -1:
                        visited[nh][nw] = count
                        next.append((nh, nw))

        if len(next) == 0:
            break
        else:
            dq.append(next)
            next = []

bfs(start[0], start[1])

for i in range(height):
    for j in range(width):
        print(visited[i][j], end=' ')
    print()




