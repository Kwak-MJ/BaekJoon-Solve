from collections import deque

n = int(input())
target_info = list(map(int, input().split()))
element_info = list(map(int, input().split()))
only_queue = deque()

for i in range(n):
    if target_info[i] == 0:
        only_queue.append(element_info[i])

m = int(input())
insert_list = list(map(int, input().split()))

for i in insert_list:
    only_queue.appendleft(i)
    print(only_queue.pop(), end=" ")
