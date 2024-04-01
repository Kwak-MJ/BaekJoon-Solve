'''
1. 아이디어
a에서 b로의 경로? -> 그래프 문제다

연결하는 비용을 최소로 한다? -> 최단경로? or MST

모든 컴퓨터가 연결되기를 원함, 직접 필요X, 연결만 되면 됨 -> MST

연결할 수 없는 경우는 없다 (고려 안해도 됨)

★ reverse=True 하는게 deque 쓰는 것보다 더 빠름
★ heapq도 더 느리게 나옴!

2. 시간 복잡도
2초 -> 4천만?
2초 -> 2억?

노드의 수 V -> 1 ~ 1000
간선의 수 E -> 1 ~ 100,000

최대로 보면, ElogE 까지는 됨

MST(Kruskal) 사용하면 -> 최선 VlogE, 최악 V * E

3. 예외 케이스
a,b,c 에서 
c는 weight
a,b 가 노드인데, a와 b가 같은 경우도 존재함!
'''
import sys
input = sys.stdin.readline

numV = int(input())
numE = int(input())

dset = [i for i in range(numV + 1)]
graph = sorted([list(map(int, input().split()))
               for _ in range(numE)], reverse=True, key=lambda x: x[2])


def find(x: int):
    while dset[x] != x:
        x = dset[x]
    return x


def union(x: int, y: int):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x > y:
        x, y = y, x

    dset[y] = x


result = []
while len(result) < numV - 1:
    u, v, w = graph.pop()
    u_parent = find(u)
    v_parent = find(v)
    if u_parent != v_parent:
        union(u, v)
        result.append(w)

print(sum(result))
