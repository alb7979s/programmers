#이분매칭 가능할듯
#그래프 모델링 해서
dic={}
idx=1
def edgeAdd(u, v, adj):
    adj[u].append(v)
    adj[v].append(u)
def graph(str, s, node):  #s시작겸 인덱스
    for i in range(len(str)-1):
        #영문만 그래프 모델링
        if 'a' <= str[i] <= 'z' and 'a' <= str[i+1] <= 'z':
            node[s] = indexing(str[i]+str[i+1])
            s+=1
    return s
def indexing(string):
    global idx, dic
    try:
        return dic[string]
    except:
        dic[string]=idx
        idx+=1
        return dic[string]
def dfs(a, A, B, visit, visitCnt, adj):
    if visit[a] == visitCnt: return False
    visit[a] = visitCnt
    for b in adj[a]:
        if B[b]==-1 or dfs(B[b], A, B, visit, visitCnt, adj):
            A[a] = b
            B[b] = a
            return True
    return False
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    node = [0] * (len(str1)+len(str2))
    uMAX = graph(str1, 0, node)
    vMAX = graph(str2, uMAX, node)
    adj = [[]for _ in range(vMAX+2)]
    for i in range(uMAX):
        for j in range(uMAX, vMAX):
            if node[i] == node[j]:
                edgeAdd(i, j, adj)
    A=[-1]*uMAX
    B=[-1]*vMAX
    visit=[-1]*uMAX
    match=0
    visitCnt=1
    for i in range(uMAX):
        match+=dfs(i, A, B, visit, visitCnt, adj)
        visitCnt+=1
    add = vMAX - match
    if vMAX==0: return 65536
    return int(match/add*65536)
solution('FRANCE','french')
