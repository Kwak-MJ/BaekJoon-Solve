class DisjointSet:
    def __init__(self, n):
        self.U = []
        for i in range(n+1):
            self.U.append(i)

    # 재귀보단 반복문이 best
    def find(self, i):  # 자신과 다를 때까지 올라가서 부모 찾기
        j = i
        while self.U[j] != j:
            j = self.U[j]
        return j

    def union(self, p, q):  # 여기서는 작은 수가 큰 수의 부모가 되도록 정함
        p = self.find(p)
        q = self.find(q)
        if (p < q):
            self.U[p] = q
        else:
            self.U[q] = p

    def equal(self, p, q):  # 같은지 확인
        if (p == q):
            return True
        else:
            return False
