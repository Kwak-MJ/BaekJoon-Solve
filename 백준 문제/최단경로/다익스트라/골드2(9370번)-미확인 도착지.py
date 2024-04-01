import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def dijkstra(graph: list, start: int):
    INF = 1e8
    d = [INF] * len(graph)
    d[start] = 0

    heapq = [(0, start)]  # (노드, 해당 노드까지의 거리) 힙에 저장
    while len(heapq) != 0:
        v_d, v = heappop(heapq)

        if d[v] < v_d:
            continue

        for i in graph[v]:
            u_w, u = i[0], i[1]
            if d[u] > u_w + v_d:
                d[u] = u_w + v_d
                heappush(heapq, (d[u], u))

    return d


test_num = int(input())

result = []
# 테스트 케이스 T < 100, T^3 까지 가능
for _ in range(test_num):
    v_num, e_num, t_num = map(int, input().split())
    v_depart, v_g, v_h = map(int, input().split())
    g_h_d = 0
    graph = [[] for _ in range(v_num+1)]
    for i in range(e_num):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
        graph[v].append((w, u))

        if u == v_g and v == v_h:
            g_h_d = w
        elif u == v_h and v == v_g:
            g_h_d = w

    v_t = []
    for _ in range(t_num):
        v_t.append(int(input()))

    d_from_depart = dijkstra(graph, v_depart)
    g_depart_d = d_from_depart[v_g]
    h_depart_d = d_from_depart[v_h]

    d_from_g = dijkstra(graph, v_g)
    d_from_h = dijkstra(graph, v_h)

    case = []
    for t in v_t:
        t_depart_d = d_from_depart[t]
        g_t_d = d_from_g[t]
        h_t_d = d_from_h[t]

        test_d = min((g_depart_d+g_h_d+h_t_d), (h_depart_d+g_h_d+g_t_d))

        if test_d == t_depart_d:
            case.append(t)

    result.append(case)

for cases in result:
    for i in sorted(cases):
        print(i, end=' ')
    print()
