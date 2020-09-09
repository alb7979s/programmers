#실제 시험처럼 시간 정해놓고 풀었는데 반례있음, 오답 정리할때 반례 고치기
#알고리즘 생각하면서 하려니까 시간이 부족하구나.. 
from sys import*
input=lambda:stdin.readline().strip()
setrecursionlimit(10**6)
def dfs(pos):
    global Set, ans, visit, res
    if pos == len(res):
        ans.append(list(Set))
        return
    for x in res[pos]:
        if x not in visit or not visit[x]:
            visit[x] = 1
            Set.add(x)
            dfs(pos+1)
            visit[x] = 0
            Set.remove(x)
def solution(user_id, banned_id):
    global Set, ans, visit, res
    res = [[] for _ in range(len(banned_id))]
    for userid in user_id:
        for i, banid in enumerate(banned_id):
            if len(userid) == len(banid):
                flag=True
                for j in range(len(userid)):
                    if banid[j] != '*' and userid[j] != banid[j]:
                        flag=False
                        break
                if flag:
                    res[i].append(userid)
    Set = set()
    ans = []
    visit = {}
    dfs(0)
    ans.sort()
    cnt=1
    for i in range(len(ans)-1):
        if ans[i] == ans[i+1]: continue
        else:cnt+=1
    # print(cnt)
    return cnt

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
