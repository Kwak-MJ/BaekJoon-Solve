# 동시에 같은 level은 1로 바뀌어야함
# bst 활용 문제
# O(n^2) 까지 가능
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def tomatoBFS(children: list, day: int, zero_num: int):
    children_pos = deque()
    children_pos.append(children)

    while children_pos:
        child_group = children_pos.popleft()
        day_child = []

        if zero_num == 0:
            break

        for child_pos in child_group:
            i, j = child_pos[0], child_pos[1]

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if group[nx][ny] == 0:
                        group[nx][ny] = 1
                        zero_num -= 1
                        day_child.append((nx, ny))

        day += 1
        if len(day_child) != 0:
            children_pos.append(day_child)

    return day, zero_num


# m이 열, n이 행
m, n = map(int, input().split())
group = []
zero_num = 0

for _ in range(n):
    insert = list(map(int, input().split()))
    zero_num += insert.count(0)
    group.append(insert)

day = 0

operator = []
for i in range(n):
    for j in range(m):
        if group[i][j] == 1:
            operator.append((i, j))

day, zero_num = tomatoBFS(operator, day, zero_num)

if zero_num == 0:
    print(day)
else:
    print(-1)
