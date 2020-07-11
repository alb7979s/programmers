from collections import*
dic={}
idx=1
def indexing(string):
    global dic, idx
    try:
        return dic[string]
    except:
        dic[string]=idx
        idx+=1
        return dic[string]
def solution(cacheSize, cities):
    if cacheSize==0:
        return len(cities)*5
    q=deque()
    ans=0
    for city in cities:
        city = city.lower()
        city = indexing(city)
        qLen = len(q)
        search=False
        for i in range(qLen):
            if q[0]==city:  #찾으면 빼놓음
                search=True
                q.popleft()
            else:
                q.append(q.popleft())
        if search:  #찾음
            ans+=1
        else:       #못찾음
            ans+=5
            if len(q)>=cacheSize:  #못찾았는데 가득참
                q.popleft()
        #찾던 못찾던 추가(찾으면 빼놓은거, 못찾으면 그냥) !!cacheSize==0이면 여기서 오류남
        q.append(city)
    return ans
