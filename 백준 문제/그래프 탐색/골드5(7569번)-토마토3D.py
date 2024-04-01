'''
1. 아이디어
대표적인 bfs

boxes = [[[0 * width] * height] * h]
boxes 의 위치를 indexing 시에는 -> boxes[3차원 높이][세로][가로] 순서

모두 익는 일수
모두 익어있는 경우 (0) -> one, mone의 합이 전체
모두 익지 못하는 경우 (-1) -> bfs 돌리고 one, zero, mone의 합이 전체


->> 차원을 축소하면 시간이 줄어듬

'''
import sys
from collections import deque
input = sys.stdin.readline

w, v, h = map(int, input().split())  # 가로, 세로, 3차원 높이
boxes = []
one_pos = []
zero = 0
one = 0
mone = 0
count = 0

dw = [1, -1, 0, 0, 0, 0]
dv = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

for hh in range(h):
    box = []
    for vv in range(v):
        box.append(list(map(int, input().split())))
    boxes.append(box)

for hh in range(h):
    for vv in range(v):
        for ii in range(w):
            if boxes[hh][vv][ii] == 0:
                zero += 1
            elif boxes[hh][vv][ii] == 1:
                one += 1
                boxes[hh][vv][ii] = 1
                one_pos.append((hh, vv, ii))
            else:
                mone += 1
                boxes[hh][vv][ii] = -1


def bfs(one_pos: list):
    global zero, one
    dq = deque([one_pos])
    day = 0

    while dq:
        now = dq.popleft()
        insert = []
        for hh, vv, ww in now:
            for j in range(6):
                cw = ww + dw[j]
                cv = vv + dv[j]
                ch = hh + dh[j]
                if 0 <= cw < w and 0 <= cv < v and 0 <= ch < h and boxes[ch][cv][cw] == 0:
                    insert.append((ch, cv, cw))
                    boxes[ch][cv][cw] = boxes[hh][vv][ww] + 1
                    zero -= 1
                    one += 1
            day = max(day, boxes[hh][vv][ww])
        if len(insert) != 0:
            dq.append(insert)
    return day


if one + mone == w*v*h:
    print(0)
else:
    count = bfs(one_pos)
    if one + mone == w*v*h:
        print(count-1)
    else:
        print(-1)
