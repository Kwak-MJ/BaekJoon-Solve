'''
1. 아이디어
다익스트라인줄 알았는데, 가중치 없음

그냥 bfs로 턴을 계산하면 될 것 같음

N이 100밖에 안되니까 for문으로 처리해서
[]에 각 사람마다 결과 저장한 뒤 sum 이용해서 최종값 비교

모두 친구로 이어짐 -> 연결 그래프임

2. 시간 복잡도
2초 
2 <= N <= 100
1 <= M <= 5000

BFS = O (N+M)
for 문에서는 N 반복

N^2 or N*M 모두 가능

3. 예외 케이스
'''
import sys
input = sys.stdin.readline

numV, numE = map(int, input().split())
graph = [[] for _ in range(numV + 1)]

for _ in range(numE):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(start: int):
    visited = [0] * (numV + 1)
    cur_dq = [start]
    visited[start] = 1
    count = [0] * (numV + 1)

    while cur_dq:
        u = cur_dq.pop(0)

        for neigh in graph[u]:
            if visited[neigh] == 0:
                visited[neigh] = 1
                count[neigh] = count[u] + 1
                cur_dq.append(neigh)

    return (i+1, sum(count))


result = []
for i in range(numV):
    result.append(bfs(i+1))


result.sort(key=lambda x: (x[1], x[0]))
print(result[0][0])
