# 아이디어
# 최대 높이가 256이므로 브루트포스 -> 모두 검사 가능
m, n, b = map(int, input().split())  # 가로 n, 세로 m

graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

time = 1e8
idx = 0

for height in range(257):
    removing, adding = 0, 0

    for i in range(m):  # 세로에서 먼저 선택
        for j in range(n):  # 가로에서 선택
            if graph[i][j] > height:
                removing += graph[i][j] - height
            else:
                adding += height - graph[i][j]

    if removing + b >= adding:
        if removing * 2 + adding <= time:
            time = removing*2 + adding
            idx = height

print(time, idx)
