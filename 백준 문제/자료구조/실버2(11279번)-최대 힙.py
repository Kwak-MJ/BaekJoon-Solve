def heapifyUp():
    index = len(max_heap) - 1
    parentIndex = (index - 1) // 2
    while parentIndex >= 0 and max_heap[parentIndex] < max_heap[index]:
        max_heap[parentIndex], max_heap[index] = max_heap[index], max_heap[parentIndex]
        index = parentIndex
        parentIndex = (index - 1) // 2


def heapifyDown():
    index = 0
    while (2*index + 1) < len(max_heap):
        smallIndex = 2*index + 1
        if (2*index + 2) < len(max_heap) and max_heap[smallIndex] < max_heap[2*index + 2]:
            smallIndex = 2*index + 2

        if max_heap[index] < max_heap[smallIndex]:
            max_heap[index], max_heap[smallIndex] = max_heap[smallIndex], max_heap[index]
            index = smallIndex
        else:
            break


def insert(e):
    max_heap.append(e)
    heapifyUp()


def removeMax():
    max_heap[0], max_heap[-1] = max_heap[-1], max_heap[0]
    result = max_heap.pop()
    heapifyDown()
    return result


max_heap = []
n = int(input())

output = []
for _ in range(n):
    given = int(input())
    if given == 0 and len(max_heap) == 0:
        output.append(0)
    elif given == 0 and len(max_heap) != 0:
        output.append(removeMax())
    else:
        insert(given)

for i in output:
    print(i)
