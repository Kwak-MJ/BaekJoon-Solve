from collections import deque
import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    n, target = map(int, input().split())
    importance = deque()
    for index, imp in enumerate(list(map(int, input().split()))):
        importance.append((index, imp))

    count = 0
    while importance:
        biggest = max(importance, key=lambda x: x[1])
        g = importance.popleft()

        if biggest[1] <= g[1]:
            count += 1
            if g[0] == target:
                break
        else:
            importance.append(g)
    print(count)
