from collections import deque

n = int(input())
A = deque(enumerate(map(int, input().split())))

while A:
    index, degree = A.popleft()
    print(index+1, end=" ")
    if degree >= 0:
        A.rotate(-degree + 1)
    else:
        A.rotate(-degree)
