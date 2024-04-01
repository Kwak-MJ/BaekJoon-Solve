from collections import deque


def topologySort(group: list, inDegree: list):
    result = []
    queue = deque()
    for i in range(1, n+1):  # O(n)
        if inDegree[i] == 0:
            queue.append(i)

    while len(queue) != 0:  # amortized O(m)
        parent = queue.popleft()
        result.append(parent)
        children = group[parent]
        for child in children:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                queue.append(child)

    return result


n, m = map(int, input().split())
group = [[] for _ in range(n+1)]  # 학생 수 만큼 정점 생성
inDegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())  # a -> b
    group[a].append(b)
    inDegree[b] += 1

result = topologySort(group, inDegree)
for i in result:
    print(i, end=' ')
