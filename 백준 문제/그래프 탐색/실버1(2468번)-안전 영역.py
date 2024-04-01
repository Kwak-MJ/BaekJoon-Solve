from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def markFalse(i: int, j: int, boolean_map: list):
    next_list = deque()
    next_list.append([(i, j)])
    boolean_map[i][j] = False

    # 정답 코드
    while next_list:
        x, y = next_list.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if boolean_map[nx][ny] == True:
                    boolean_map[nx][ny] = False
                    next_list.append((nx, ny))

    # 메모리 초과 코드
    # while len(next_list) != 0:
    #     next = next_list.popleft()

    #     for child in next:
    #         x, y = child
    #         boolean_map[x][y] = False
    #         day_child = []

    #         if x-1 >= 0 and boolean_map[x-1][y] == True:
    #             day_child.append((x-1, y))

    #         if x+1 < n and boolean_map[x+1][y] == True:
    #             day_child.append((x+1, y))

    #         if y-1 >= 0 and boolean_map[x][y-1] == True:
    #             day_child.append((x, y-1))

    #         if y+1 < n and boolean_map[x][y+1] == True:
    #             day_child.append((x, y+1))

    #     if len(day_child) == 0:
    #         break

    #     next_list.append(day_child)


n = int(input())
height_map = []

max_value = 0
for _ in range(n):  # O(n^2) 소요 OK
    insert_list = list(map(int, input().split()))
    if max_value < max(insert_list):
        max_value = max(insert_list)
    height_map.append(insert_list)


# i 이하인 지역이 물에 잠김
# 1부터 (max_value-1)까지
# max_value는 최대 100번 반복
# 최대 100회 반복인 for문 3회까지 가능
safe_max = 0
for i in range(max_value):  # O(n^3) 소요 OK
    boolean_map = [[False]*n for _ in range(n)]

    for p in range(n):
        for q in range(n):
            if height_map[p][q] > i:
                boolean_map[p][q] = True

    tmp = 0
    for e in range(n):
        for r in range(n):
            if boolean_map[e][r] == True:
                tmp += 1
                markFalse(e, r, boolean_map)

    safe_max = max(safe_max, tmp)

print(safe_max)
