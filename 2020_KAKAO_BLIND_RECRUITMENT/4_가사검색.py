'''
그냥 하나의 트라이로 구현 했을 때 ?가 접두사에 위치하면 트라이 쓴 이유가 사라짐(다 찾아봐야함)
그래서 정방향, 거꾸로 된 두개의 트라이 구현하고 ?위치에 따라서 탐색(앞이면 거꾸로, 뒤면 그대로)
? 만났을 때 몇개나 되는지는 배열에 저장해놓을 수 있음

제한사항에 ?가 접두사, 접미사에 주어진다는게 힌트이자 열쇠인듯..
'''
import sys
from collections import*
sys.setrecursionlimit(10**6)
input = lambda:sys.stdin.readline().strip()
class Node:
    def __init__(self):
        self.end = False
        self.child = {}
        self.mem = {}
class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self, string):
        node = self.root      #루트로 시작
        ls = len(string)
        for i, char in enumerate(string):
            if ls not in node.mem: node.mem[ls]=1
            else: node.mem[ls] += 1                                 #이 당시의 노드 일 때 ls길이의 글자 개수 증가
            if char not in node.child: node.child[char] = Node()    #자식에 없을때만 추가
            node = node.child[char]                                 #다음 노드로
            # if node.end: return False
        node.end = True
        # return True
    def search(self, string):
        q=deque()
        q.append(self.root)
        ls = len(string)
        res=0
        for s in string:
            lq = len(q)
            for i in range(lq):
                node = q.popleft()
                if s=='?':
                    if ls in node.mem:
                        return node.mem[ls]
                    return 0
                elif s in node.child:
                    q.append(node.child[s])
        while q:
            node = q.poplfet()
            if node.end: res+=1
        return res

'''처음에 트라이 하나로 무식하게 탐색하다가 효율성 못넘김
    def search(self, string):
        q=deque()
        q.append(self.root)
        for s in string:
            lq = len(q)
            for i in range(lq):
                x = q.popleft()
                if s=='?':
                    for k, v in x.child.items():
                        q.append(v)
                elif s in x.child:
                    q.append(x.child[s])
        cnt=0
        while q:
            x = q.popleft()
            if x.end: cnt+=1
        return cnt
'''
def solution(words, queries):
    trie = Trie()
    trieReverse = Trie()
    for word in words:
        trie.insert(word)
        trieReverse.insert(word[::-1])
    res=[]
    for query in queries:
        if query[0]=='?':
            res.append(trieReverse.search(query[::-1]))
        else:
            res.append(trie.search(query))
    return res
solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
