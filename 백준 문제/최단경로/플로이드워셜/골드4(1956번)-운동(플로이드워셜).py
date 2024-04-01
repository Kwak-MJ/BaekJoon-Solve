# 일방 통행 -> digraph
# 노드 번호는 1번부터
# 운동을 위한 경로 -> 최단 사이클
# 두 마을을 왕복하는 것도 사이클
n, m = map(int, input().split())
INF = 1e8
graph = [[INF] * (n+1) for _ in range(n+1)]


for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u][v] = w


for k in range(1, n+1):
    for j in range(1, n+1):
        for i in range(1, n+1):
            graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j])

result = INF
for i in range(1, n+1):
    result = min(graph[i][i], result)

if result == INF:
    print(-1)
else:
    print(result)
