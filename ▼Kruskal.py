# E는 오름차순으로 정렬된 엣지리스트(가중치, end 점들)
def kruskal(n: int, E: list):
    minSTE = []
    dset = DisjointSet(n)
    while len(E) < n-1:
        edge = E.pop()
        i, j = edge[0], edge[1]
        p = dset.find(i)
        q = dset.find(j)
        if not dset.equal(p, q):
            dset.union(p, q)
            minSTE.append(edge)

    return minSTE


class DisjointSet:
    def __init__(self, n):
        self.U = []
        for i in range(n):
            self.U.append(i)

    def find(self, i):  # 자신과 다를 때까지 올라가서 부모 찾기
        j = i
        while self.U[j] != j:
            j = self.U[j]
        return j

    def union(self, p, q):
        if (p < q):
            self.U[p] = q
        else:
            self.U[q] = p

    def equal(self, p, q):
        if (p == q):
            return True
        else:
            return False
