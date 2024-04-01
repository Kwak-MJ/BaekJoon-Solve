'''
1. 아이디어
재귀? 분할정복?

한 변의 길이 n
sum이 n^2 이거나 0이면 멈춰
둘 다 아니라면 또 4등분 실시

n = 1까지 진행

white
blue 카운트 진행

2. 시간 복잡도
n의 범위 2,4,8,16,32,64,128 중 하나

3. 예외 케이스
'''
import sys
input = sys.stdin.readline

n = int(input())
graph = []
white = 0
blue = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))  # 행, 열


def check(graph: list):
    global white
    global blue

    l = len(graph)
    if l == 1:
        if graph[0][0] == 1:
            blue += 1
        else:
            white += 1
        return

    sum = 0
    for i in range(l):
        for j in range(l):
            sum += graph[i][j]

    if sum == 0:
        white += 1
        return
    elif sum == l**2:
        blue += 1
        return

    next = []
    for i in range(l//2):
        insert = graph[i][:l//2]
        next.append(insert)
    check(next)

    next = []
    for i in range(l//2):
        insert = graph[i][l//2:]
        next.append(insert)
    check(next)

    next = []
    for i in range(l//2, l):
        insert = graph[i][:l//2]
        next.append(insert)
    check(next)

    next = []
    for i in range(l//2, l):
        insert = graph[i][l//2:]
        next.append(insert)
    check(next)


check(graph)
print(white)
print(blue)
