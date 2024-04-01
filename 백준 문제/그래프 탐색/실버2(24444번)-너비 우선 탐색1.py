# 일반적인 무방향 dfs 에서는 인접 정점을 오름차순으로 탐색
import sys
from collections import deque

c = 1


def bfs(r):  # 글로벌 써야됨. 재귀함수라서 매개변수로 주면 안됨, 별개의 값
    global c
    que.append(r)
    visited[r] = c
    while len(que) != 0:
        v = que.popleft()
        for i in sorted(graph[v]):
            if visited[i] == 0:
                c += 1
                visited[i] = c
                que.append(i)


sys.setrecursionlimit(200000)  # 재귀함수 주의!
n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]  # 단순히 곱하기 하면 같은 주소 리스트가 복사되어버림
que = deque()
visited = [0] * (n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


bfs(r)

for i in visited[1:]:
    print(i)
