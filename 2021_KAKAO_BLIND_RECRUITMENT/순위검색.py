class Node:
    def __init__(self):
        self.child = {}
class Trie:
    def __init__(self):
        self.root = Node()
        self.sorted = set()
    def insert(self, node, data, score):
        if not data:
            if not node.child:
                node.child = []
            node.child.append(score)
            return
        addData = data[0]
        if addData not in node.child:
            node.child[addData] = Node()
        self.insert(node.child[addData], data[1:], score)
        if '-' not in node.child:
            node.child['-'] = Node()
        self.insert(node.child['-'], data[1:], score)

    def lower(self, data, score):
        l = 0
        r = len(data) - 1
        while l <= r:
            mid = (l+r)//2
            if data[mid] < score:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def search(self, data, score):
        node = self.root
        for d in data:
            if d not in node.child: return 0
            node = node.child[d]
        if node not in self.sorted:
            node.child.sort()
            self.sorted.add(node)
        return len(node.child) - self.lower(node.child, score)
def solution(info, query):
    trie = Trie()
    for str in info:
        data = str.split()
        trie.insert(trie.root, data[:-1], int(data[-1]))
    res = []
    for str in query:
        data = str.split(" and ")
        data[-1], score = data[-1].split()
        res.append(trie.search(data, int(score)))
    return res
