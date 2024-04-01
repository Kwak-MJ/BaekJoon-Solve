import heapq

heap = []
n = int(input())

output = []

for _ in range(n):
    given = int(input())
    if given == 0:
        if len(heap) == 0:
            output.append(0)
        else:
            output.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap, given)

for i in output:
    print(i)
