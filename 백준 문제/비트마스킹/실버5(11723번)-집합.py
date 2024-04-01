import sys
input = sys.stdin.readline

object = []
visited = [False] * 21

n = int(input())
for _ in range(n):
    given = input().rstrip()

    if given[-1].isdigit():
        order, num = given.split()
        num = int(num)
    else:
        order = given

    if order == 'add':
        if visited[num] == False:
            visited[num] = True
    elif order == 'check':
        if visited[num] == True:
            print(1)
        else:
            print(0)
    elif order == 'remove':
        if visited[num] == True:
            visited[num] = False
    elif order == 'toggle':
        if visited[num] == True:
            visited[num] = False
        else:
            visited[num] = True
    elif order == 'all':
            visited = [True] * 21
    elif order == 'empty':
            visited = [False] * 21