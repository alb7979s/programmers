#set()에 넣고
#two-pointer로 처리
def solution(gems):
    Set = set()
    for gem in gems:
        Set.add(gem)
    lg = len(gems)
    lgs = len(Set)       #보석 종류의 개수
    dic={}
    for x in Set:       #모든 보석 0으로 초기화
        dic[x] = 0
    s, e = 0, 0
    cnt = 0
    ans=[]
    while e<lg:
        if cnt < lgs:           #보석 개수 안되면 뒤로 확장
            if not dic[gems[e]]:
                cnt += 1
            dic[gems[e]] += 1
            e += 1
        while cnt >= lgs:
            ans.append((s, e-1, (e-1)-s))
            dic[gems[s]] -= 1
            if not dic[gems[s]]:cnt-=1
            s += 1
    ans.sort(key=lambda x:x[2])
    # print(ans)
    return [ans[0][0]+1, ans[0][1]+1]
solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
