# solved.ac 104 레이팅, 실버2 문제 = -7
# 정점번호  1부터 N까지
# 내림차순 너비우선탐색
from collections import deque

v_num, e_num, v_start = map(int, input().split())
group = [[] for _ in range(v_num+1)]
visited = [0] * (v_num+1)
c = 1

for _ in range(e_num):
    u, v = map(int, input().split())
    group[u].append(v)
    group[v].append(u)


def bfs(start: int):
    global c
    que = deque()
    que.append(start)
    visited[start] = c

    while que:
        v = que.popleft()
        children = sorted(group[v], reverse=True)
        for child in children:
            if visited[child] == False:
                c += 1
                visited[child] = c
                que.append(child)


bfs(v_start)

for j in visited[1:]:
    print(j)
