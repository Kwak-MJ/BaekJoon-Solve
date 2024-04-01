'''
1. 아이디어
그래프 탐색으로 금방 풀릴 듯

2. 시간 복잡도
O(v+e) 가능

3. 예외
예외는 아니지만, union-find로 상위 기록을 만들 수 있는듯
'''
import sys
from collections import deque

input = sys.stdin.readline

v_num, e_num = map(int, input().split())
graph = [[] for _ in range(v_num+1)]
visited = [False] * (v_num+1)

for _ in range(e_num):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    dq = deque([start])
    visited[start] = True

    while dq:
        cur = dq.popleft()
        for next in graph[cur]:
            if visited[next] == False:
                visited[next] = True
                dq.append(next)

cc_count = 0
for i in range(1, v_num+1):
    if visited[i] == False:
        bfs(i)
        cc_count += 1

print(cc_count)