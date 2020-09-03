#아예 content만 찾아서 dic값 있는 애들만 찾고
#그 다음 다시 반복문 돌려서 dic에 있으면 연결 없으면 outdegree개수만 ++
dic={}
idx=0
def indexing(string):
    global idx, dic
    try:
        return dic[string]
    except:
        dic[string] = idx
        idx+=1
        return dic[string]
class Info:
    def __init__(self):
        self.default = 0
        self.link = 0
        self.indegree = []
        self.outdegree = 0

def solution(word, pages):
    a=[]
    word=word.lower()
    info = [Info() for _ in range(21)]
    #indexing
    for i in range(len(pages)):
        pages[i] = pages[i].lower()
        page = pages[i].split('<')
        for x in page:
            if 'meta' in x and 'http' in x:
                xsplit = x.split('"')
                for j in range(len(xsplit)):
                    if 'http' in xsplit[j]:
                        indexing(xsplit[j])
    #link check
    for i in range(len(pages)):
        pages[i] = pages[i].lower()
        page = pages[i].split('<')
        for x in page:
            if 'a href' in x:
                xsplit = x.split('"')
                for j in range(len(xsplit)):
                    if 'http' in xsplit[j]:
                        v = indexing(xsplit[j])
                        info[v].indegree.append(i)
                        info[i].outdegree+=1
    # word 찾기
    for i in range(len(pages)):
        page = pages[i]
        res=''
        for j in range(len(page)):
            if 'a'<=page[j]<='z': res+=page[j]
            else: res+=' '
        pages[i] = res.split()
    u=0
    for page in pages:
        for x in page:
            if word==x:
                info[u].default+=1
        u+=1
    MAX = [-1, -1]
    for index, i in enumerate(info):
        res = i.default
        for v in i.indegree:
            ex = info[v].outdegree
            if not ex: continue
            res += (info[v].default / ex)
        if MAX[0] < res:
            MAX = [res, index]
    return MAX[-1]
