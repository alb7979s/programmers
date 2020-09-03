from sys import*
setrecursionlimit(10**6)
class Node:
    def __init__(self, key, data):      #x가 data, key노드번호
        self.key = key
        self.data = data
        self.left = self.right = None

class BST:
    def __init__(self):     #root만 y로 찾고, 나머지 x, i로 만듦
        self.root = None
    def insert(self, key, data):
        self.root = self._insert(self.root, key, data)
    def _insert(self, node, key, data):
        if node is None: node = Node(key, data)
        else:
            if node.data < data: node.right = self._insert(node.right, key, data)
            if node.data > data: node.left = self._insert(node.left, key, data)
        return node
    def preorder(self):
        temp=[]
        self._preorder(self.root, temp)
        return temp
    def _preorder(self, node, temp):
        if node is None: return
        temp.append(node.key)
        self._preorder(node.left, temp)
        self._preorder(node.right, temp)
    def postorder(self):
        temp=[]
        self._postorder(self.root, temp)
        return temp
    def _postorder(self, node, temp):
        if node is None: return
        self._postorder(node.left, temp)
        self._postorder(node.right, temp)
        temp.append(node.key)
def solution(nodeinfo):
    ans = []
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key=lambda x: x[1], reverse=True)
    bst = BST()
    for x, y, i in nodeinfo:
        bst.insert(i, x)
    ans.append(bst.preorder())
    ans.append(bst.postorder())
    return ans
