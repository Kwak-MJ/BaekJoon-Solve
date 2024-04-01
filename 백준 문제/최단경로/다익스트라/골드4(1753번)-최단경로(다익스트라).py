import sys
import io
import os
from heapq import heappop, heappush
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
INF = 1e8

# 노드, 간선 개수
n, m = map(int, input().split())

# 시작 노드 입력
start = int(input())

# 그래프 2차원 배열
graph = [[] for _ in range(n+1)]
# 그래프 업데이트 필요**
# (인접노드, 가중치) 형태로 추가
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):
    # 거리 값 저장 배열
    distance = [INF] * (n+1)
    distance[start] = 0

    heap = [(0, start)]

    while heap:
        du, u = heappop(heap)

        # 힙에는 같은 정점이라해도 업데이트가 안됨, 쌓이는중
        # distance는 항상 업데이트 되므로 미리 확인
        if distance[u] < du:
            continue

        for k in graph[u]:
            v = k[0]
            w = k[1]
            if du + w < distance[v]:
                distance[v] = du + w
                heappush(heap, (distance[v], v))

    return distance


d = dijkstra(start)
for i in d[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)
