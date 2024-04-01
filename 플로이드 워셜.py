# n 이 100
# 노드들 사이의 방향이 미리 정해져 있지 않음
# 우리가 자유롭게 정할 수 있음
import sys
input = sys.stdin.readline

n = int(input())  # 도시의 수
m = int(input())  # 버스의 수
INF = 1e8
group = [[INF] * (n+1) for _ in range(n+1)]

# a->a 경로의 비용은 0 으로 초기화
for i in range(1+n):
    group[i][i] = 0

# 버스들의 노선 및 비용 저장
for _ in range(m):
    a, b, cost = map(int, input().split())
    group[a][b] = min(cost, group[a][b])  # 노선이 여러 개 들어오는 경우...


# 3중 반복문으로 a->k k->b 가 최단경로인지 계산
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            group[a][b] = min(group[a][b], group[a][k]+group[k][b])

# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        g = group[i][j]
        if g == INF:
            print(0, end=' ')
        else:
            print(g, end=' ')
    print()
