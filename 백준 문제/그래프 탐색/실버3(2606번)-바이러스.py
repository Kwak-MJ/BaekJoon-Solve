'''
1. 아이디어
연결 그래프에서 바이러스 전파됨
비연결인 경우에는 지장 없음

항상 1번 컴퓨터가 먼저 감염

dfs or bfs로 1번이 이루는 연결 그래프 파악

2. 시간 복잡도
1초 -> 2천만
v+e,
v 100이하 e는 기준 없음

3. 예외 케이스

'''
import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
visited = [0] * (v+1)


def bfs(start: int):
    visited[start] = 1
    q = deque([start])

    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if visited[next] == 0:
                visited[next] = 1
                q.append(next)


for _ in range(e):
    u, k = map(int, input().split())
    graph[u].append(k)
    graph[k].append(u)

bfs(1)

print(sum(visited)-1)
