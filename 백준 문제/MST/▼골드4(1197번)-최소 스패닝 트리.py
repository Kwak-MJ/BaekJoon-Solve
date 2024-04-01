import sys
input = sys.stdin.readline


def find(x: int):  # path compression
    if U[x] != x:
        U[x] = find(U[x])

    return U[x]


def union(u: int, v: int):
    u = find(u)
    v = find(v)
    if u == v:
        return

    if u > v:
        u, v = v, u

    U[v] = u


numV, numE = map(int, input().split())
graph = sorted([list(map(int, input().split()))
               for _ in range(numE)], reverse=True, key=lambda x: x[2])

U = [i for i in range(numV + 1)]


MST = []
while len(MST) < numV-1:  # numV-1 해주기 주의해야됨
    u, v, w = graph.pop()
    u_parent = find(u)
    v_parent = find(v)
    if u_parent != v_parent:
        union(u, v)
        MST.append(w)

print(sum(MST))
