#unionFind 썼는데, k가 10**12라서 그냥 초기화 하는데에도 시간초과 뜸
#dict()로 처리해서 통과했는데 여기서 C++로 바꿔 풀다가 시간 다잡아먹은듯
from sys import*
input=lambda:stdin.readline().strip()
setrecursionlimit(10**6)
class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.last = {}
    def find(self, u):
        if u not in self.parent:
            self.parent[u] = u
            self.last[u] = u
        if self.parent[u] == u: return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self, u, v):
        #u < v
        u = self.find(u)
        v = self.find(v)
        #합치기
        self.parent[v] = u
        #last 갱신
        ret = self.last[u]
        self.last[u] = self.last[v]
        return ret
def solution(k, room_number):
    uf = UnionFind(k)
    res=[]
    for r in room_number:
        r = uf.find(r)
        res.append(uf.union(uf.last[r], uf.last[r]+1))
    # print(res)
    return res
solution(	10, [1, 3, 4, 1, 3, 1])
