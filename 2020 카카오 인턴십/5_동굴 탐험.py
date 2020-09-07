#효율성 5번 시간초과 위상정렬로는 못푸는건가?
from collections import*
#경로 다 구한다음에 topol Sort
class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
def dfs(node, prevNode):   #dfs에 노드로 처리하면 되지 않아?
    global adj, visit, dic
    if prevNode != -1:     #초기 prev -1로 해서 루트 처리
        node.prev = prevNode
    for v in adj[node.value]:
        if not visit[v]:
            visit[v]=1
            dfs(Node(v), node)
    dic[node.value] = node
def search(node):
    global adj2, indegree, visit, check
    while 1:
        u = node.value
        visit[u] = 1
        if not u: return
        if not check[node.prev.value][u]:
            adj2[node.prev.value].add(u)
            check[node.prev.value][u]=1
            indegree[u]+=1
        node = node.prev
def solution(n, path, order):
    global adj, visit, dic, adj2, indegree, check
    adj = [[]*n for _ in range(n)]
    dic = {}
    visit=[0]*n
    visit[0]=1
    check=[[0]*n for _ in range(n)]
    for u, v in path:
        adj[u].append(v)
        adj[v].append(u)
    root = Node(0)
    dfs(root, -1)
    adj2=[set() for _ in range(n)]
    visit=[0]*n
    indegree=[0]*n
    for u, v in order:
        if not visit[u]:
            search(dic[u])
        if not check[u][v]:
            check[u][v]=1
            adj2[u].add(v)
            indegree[v]+=1
    q=deque()
    for i in range(n):
        if not indegree[i]: q.append(i)
    for i in range(n):
        if not q: return False
        u = q.popleft()
        for v in adj2[u]:
            indegree[v] -= 1
            if not indegree[v]: q.append(v)
    return True

solution(	9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]])
