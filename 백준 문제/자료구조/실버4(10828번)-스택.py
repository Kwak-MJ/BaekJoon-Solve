import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    given = list(input().split())
    if len(given) == 2:
        order, num = given[0], int(given[1])
    else:
        order = given[0]

    if order == 'push':
        stack.append(num)
    elif order == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif order == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
