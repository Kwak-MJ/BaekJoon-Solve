import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
que = deque()

for _ in range(n):
    given = list(input().split())
    if len(given) == 2:
        order, num = given[0], int(given[1])
    else:
        order = given[0]

    if order == 'push_front':
        que.appendleft(num)
    elif order == 'push_back':
        que.append(num)
    elif order == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif order == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
    elif order == 'size':
        print(len(que))
    elif order == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif order == 'pop_front':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif order == 'pop_back':
        if que:
            print(que.pop())
        else:
            print(-1)
