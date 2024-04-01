import heapq

plus_heap = []
minus_heap = []

n = int(input())
output = []

for _ in range(n):
    given = int(input())
    if given == 0:
        if len(plus_heap) == 0 and len(minus_heap) == 0:
            output.append(0)
        elif len(plus_heap) == 0:
            output.append(-(heapq.heappop(minus_heap)))
        elif len(minus_heap) == 0:
            output.append(heapq.heappop(plus_heap))
        else:
            if plus_heap[0] < minus_heap[0]:
                output.append(heapq.heappop(plus_heap))
            else:
                output.append(-(heapq.heappop(minus_heap)))
    elif given > 0:
        heapq.heappush(plus_heap, given)
    else:
        heapq.heappush(minus_heap, -(given))

for i in output:
    print(i)
