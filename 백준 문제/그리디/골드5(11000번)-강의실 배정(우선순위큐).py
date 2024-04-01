# 회의실 문제와 다름 주의
# heap 이용
import heapq
n = int(input())
table = []

for _ in range(n):
    start, end = map(int, input().split())
    table.append((start, end))

table = sorted(table, key=lambda x: (x[0], x[1]))  # 중요 부분(시작하는 시간 오름차순3)

count = 0
heap = [table[0][1]]  # 처음 끝나는 시간

for i in range(1, n):
    if heap[0] <= table[i][0]:
        heapq.heappop(heap)  # 이전 끝나는 시간 빼주기
    heapq.heappush(heap, table[i][1])  # 현재 끝나는 시간 추가해주기

print(len(heap))
